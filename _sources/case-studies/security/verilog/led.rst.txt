LED Blinker (Verilog)
======================

LED Blinker Modules
-----------------------------

In this case study, we analyze a few Verilog implementations of LED blinker modules. These modules are designed to control the blinking behavior of LEDs based on input signals and timing parameters.

The Verilog code for the LED blinker modules can be found in the repository here: `https://github.com/HyperQB/HyperRUSTY/tree/verilog_integration/benchmarks/verilog/LED <https://github.com/HyperQB/HyperRUSTY/tree/verilog_integration/benchmarks/verilog/LED>`_.

The case study was sourced from the MCHyper repository: `https://github.com/reactive-systems/MCHyper/tree/master/case-studies/asynchronous-hyperltl_2021/spi <https://github.com/reactive-systems/MCHyper/tree/master/case-studies/asynchronous-hyperltl_2021/spi>`_.

The LED blinker modules typically include inputs for clock signals and reset signals.

The first module is a simple blinker with one LED that toggles its LED state each clock cycle.  Despite this, there is an extra internal state based on the status of the up signal, which is not observable from the LED output alone.

.. code-block:: text

    module light(input clock, input up, output light_out);
        parameter [1:0] STATE_0 = 2'b00, STATE_1 = 2'b01, STATE_2 = 2'b10;
        parameter ON = 1'b1, OFF = 1'b0;
        
        reg l = OFF;
        reg [1:0] state123 = STATE_0;
        
        always @(posedge clock)
        begin
            case (state123)
                STATE_0: 
                begin
                    if (up) begin
                        state123 <= STATE_1;
                        l <= ON;
                    end else begin
                        state123 <= STATE_2;
                        l <= ON;
                    end
                end
                
                STATE_1:
                begin
                    state123 <= STATE_0;
                    l <= OFF;
                end
                
                STATE_2:
                begin
                    state123 <= STATE_0;
                    l <= OFF;
                end
            endcase
        end
        
        assign light_out = l;
    endmodule

The second module is slightly more complex, with five LEDs which light up from the least-significant LED upward and then shrinks back down, with a blanking tick between every visible frame. On each rising clock edge, a synchronous reset loads a starting pattern (LEDs=10101, led_state=010, up=0, on=1), but the very next active cycle the on flag forces LEDs to 00000 and clears on to 0, creating a one-cycle all-off “strobe.” Thereafter the logic alternates: when on==0 it outputs the next bar pattern and advances the state, then sets on<=1; when on==1 it blanks (LEDs<=00000) and sets on<=0. The patterns produced on the non-blank cycles are contiguous 1s starting at bit 0 (rightmost LED): 00001 → 00011 → 00111 → 01111 → 11111 → 01111 → 00111 → 00011 → back to 00001, i.e., grow from 1 to 5 LEDs, then shrink to 1, and repeat. The led_state values 010,011,100,101 represent the mid/upper “bar lengths,” while the “default” branch handles the edge cases (000/001/...) to insert the 1-LED and housekeeping steps; the up flag is the direction bit that flips to 0 at the top (after reaching 11111) and back to 1 at the bottom (when returning to a single lit LED).


Properties
----------
There are four properties we want to verify about these two LED blinker modules.

EA Hyperliveness Property for the 5-LED Blinker
^^^^^^^^^^^
.. math::

    \exists \pi_A.\forall \pi_B.\ \Diamond (\mathrm{LED0}_{\pi_A} \leftrightarrow \mathrm{LED0}_{\pi_B}).

This formula states that there exists a trace :math:`\pi_A` such that for all traces :math:`\pi_B`, eventually the state of the least-significant LED (LED0) in both traces will be the same. This property ensures that the blinking behavior of the least-significant LED is observable across different executions of the module.

This is satisfiable because by choosing a trace where the reset signal is always high, we can ensure that all other traces will eventually have the least-significant LED in the same state.

The formula can be found file here: `https://github.com/HyperQB/HyperRUSTY/blob/verilog_integration/benchmarks/verilog/LED/formula_ea.hq <https://github.com/HyperQB/HyperRUSTY/blob/verilog_integration/benchmarks/verilog/LED/formula_ea.hq>`_.

AE Hyperliveness Property for the 5-LED Blinker
^^^^^^^^^^^

.. math::

    \forall \pi_A.\exists \pi_B.\Box(\neg(\mathrm{reset}_{\pi_A} \land \mathrm{reset}_{\pi_B})) \rightarrow
    \bigcirc\Box(\neg\mathrm{reset}_{\pi_A} \land \neg \mathrm{reset}_{\pi_B}) \land \Diamond (\neg(\mathrm{LEDs}_{\pi_A} \leftrightarrow \mathrm{LEDs}_{\pi_B})).

This formula states that for all traces :math:`\pi_A`, there exists a trace :math:`\pi_B` such that if the reset signals in both traces are never high simultaneously, then after the initial state, both traces will eventually have different LED patterns. This property ensures that there is always a possibility of divergence in the LED patterns when the reset signals are not active.

This is satisfiable because we can choose a trace where the reset signal is always low, allowing for different LED patterns to emerge in other traces.

The formula can be found here: `https://github.com/HyperQB/HyperRUSTY/blob/verilog_integration/benchmarks/verilog/LED/formula_ae.hq <https://github.com/HyperQB/HyperRUSTY/blob/verilog_integration/benchmarks/verilog/LED/formula_ae.hq>`_.

EE Hypersafety Property 1 for the 1-LED Blinker
^^^^^^^^^^^

.. math::

    \exists \pi_A.\exists \pi_B.\Box(\mathrm{light\_out}_{\pi_A} \leftrightarrow \mathrm{light\_out}_{\pi_B}).

This formula states that there exist two traces :math:`\pi_A` and :math:`\pi_B` such that the output of the LED (light_out) is always the same in both traces. This property ensures that there are at least two executions of the module where the LED behaves identically at all times.

This is satisfiable because any two traces that start with the same initial conditions and receive the same input signals will produce identical LED outputs, despite the internal state differences.

The formula can be found here: `https://github.com/HyperQB/HyperRUSTY/blob/verilog_integration/benchmarks/verilog/LED/formula_ee_f.hq <https://github.com/HyperQB/HyperRUSTY/blob/verilog_integration/benchmarks/verilog/LED/formula_ee_f.hq>`_.

EE Hypersafety Property 2 for the 1-LED Blinker
^^^^^^^^^^^

.. math::

    \exists \pi_A.\exists \pi_B.\Box(\neg(\mathrm{light\_out}_{\pi_A} \leftrightarrow \mathrm{light\_out}_{\pi_B})).

This formula states that there exist two traces :math:`\pi_A` and :math:`\pi_B` such that the output of the LED (light_out) is never the same in both traces. This property ensures that there are at least two executions of the module where the LED behaves differently at all times.

This is unsatisfiable, as the LED behavior is deterministic, and there are no two traces that will diverge.

The formula can be found here: `https://github.com/HyperQB/HyperRUSTY/blob/verilog_integration/benchmarks/verilog/LED/formula_ee_t.hq <https://github.com/HyperQB/HyperRUSTY/blob/verilog_integration/benchmarks/verilog/LED/formula_ee_t.hq>`_.