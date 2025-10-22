Observational Determinism (Verilog)
======================

SPI Bus Secondary
-----------------------------

In this case study, we examine a Verilog implementation of an SPI (Serial Peripheral Interface) bus secondary module. The SPI protocol is widely used for communication between microcontrollers and peripheral devices. The controller manages data transmission and reception over the SPI bus, handling various modes of operation and clock configurations.

This design is sourced from the MCHyper repository: `https://github.com/reactive-systems/MCHyper <https://github.com/reactive-systems/MCHyper>`_. The adapted Verilog code we used for our analysis can be found here: `https://github.com/HyperQB/HyperRUSTY/tree/verilog_integration/benchmarks/verilog/SPI <https://github.com/HyperQB/HyperRUSTY/tree/verilog_integration/benchmarks/verilog/SPI>`_.

The role of the SPI secondary is to receive data from the SPI controller and respond accordingly. The module includes various signals for data input/output, clock management, and control flags.

.. code-block:: text

    module SPISlave(
    input clk,
    input stutter_in,
    // SPI
    input sclk_in,
    input mosi_in,
    input ss_in,
    output reg miso,
    output reg byte_transfered, 
    output reg sclk,
    output reg mosi,
    output ss,
    output reg st,
    output reg rising_sclk_edge,
    output reg falling_sclk_edge,
    output reg start,
    // Additional Input and Outputs
    input[7:0] send_item
    );

SPISlave runs off a local system clock clk and takes the master's SPI signals: sclk_in (serial clock), mosi_in (master-out, secondary-in), and ss_in (chip-select, active low). It also has a stutter_in gate that, when high, freezes the interface logic. The module drives miso (secondary-out) back to the master, and exposes a few synchronized/diagnostic copies of the incoming lines: sclk, mosi, and ss are the debounced, clock-domain-crossed versions of sclk_in, mosi_in, and ss_in respectively. Edge detectors raise one-cycle strobes rising_sclk_edge and falling_sclk_edge around sclk_in. start pulses for one cycle when ss_in asserts (transaction start). byte_transfered is a sticky flag that goes high after 8 bits have been shifted out on MISO and is cleared when ss_in deasserts. The st output mirrors the synchronized stutter_in. Finally, send_item[7:0] is a parallel preload value that seeds the transmit shift register once, on the first active cycle after reset.

.. code-block:: text

    if (!ss_v) begin
                // receiving
                if(rising_edge) begin
                    if(!byte_received) begin
                        rx_pos <= (rx_pos + 4'b0001) % 8;
                        rx_buffer <= {rx_buffer[6:0], mosi_v};
                        byte_received <= (rx_pos == 4'b0111);
                    end 
                end
                //sending
                if(falling_edge) begin
                    if(!byte_transfered) begin
                        tx_pos <= (tx_pos + 4'b0001) % 8;
                        miso <= tx_buffer[tx_pos];
                        byte_transfered <= (tx_pos == 4'b0111);
                    end
                end
            end else begin
                byte_received <= 1'b0;
                byte_transfered <= 1'b0;
            end
            //outputs
            sclk <= sclk_v;
            mosi <= mosi_v;
            en <= ~ss_v;
            st <= stutter_v;
            rising_sclk_edge <= rising_edge;
            falling_sclk_edge <= falling_edge;
            prev_en <= ~ss_v;
            start <= ({prev_en,~ss_v} == 2'b01);

On each clk edge, the module first synchronizes sclk_in, mosi_in, ss_in, and stutter_in into the local clock domain. If stutter_in is deasserted and the chip-select is active (ss_in == 0), it implements SPI mode-0 timing: on every rising edge of sclk_in it samples mosi_v into an 8-bit rx_buffer and advances rx_pos; on every falling edge it drives miso from the transmit buffer tx_buffer[tx_pos] and advances tx_pos. After the 8th bit (when the position counter reaches 7), it latches byte_received internally for RX and raises byte_transfered for TX; both counters and the flags are cleared when ss_in goes high. The outputs sclk, mosi, and ss present the synchronized views of the respective inputs for downstream logic, while start is asserted for one cycle on the 0→1 transition of the internal “enable” (i.e., when a new SPI frame begins). The transmit buffer is initialized exactly once from send_item immediately after reset, so the first outbound byte shifted on MISO is that preload; subsequent bytes will repeat unless external logic later rewrites tx_buffer (which this snippet does not do).

Property
----------

The property we want to verify is observational determinism, which ensures that for any two executions of the SPI secondary module with the same observable inputs, the observable outputs remain indistinguishable to an external observer.