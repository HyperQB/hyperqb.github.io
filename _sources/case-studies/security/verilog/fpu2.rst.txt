Constant-Time Execution (Verilog)
======================

Floating Point Unit (FPU)
-----------------------------

This case study involves verifying that a floating-point unit (FPU) implementation in Verilog executes in constant time, regardless of the input values. The FPU performs various arithmetic operations, and it is crucial to ensure that the execution time does not leak any sensitive information about the operands.

The full Verilog code for the FPU can be found in the benchmark repository `here <https://github.com/HyperQB/HyperRUSTY/tree/verilog_integration/benchmarks/verilog/divider>`_. This case study was sourced from the IODINE tool's benchmarks `here <https://github.com/gokhankici/iodine>`_.

The Verilog module under consideration implements a simple FPU that supports addition, subtraction, multiplication, and division of floating-point numbers. The design includes control logic to handle different operations and edge cases, such as overflow and underflow.

Here we are interested in verifying that the execution time of the FPU is independent of the specific values of the input operands, thus ensuring that no timing side-channel information can be inferred by an attacker.

HyperQB is able to discover a violation of this property in the division operation, where certain input values lead to longer execution times due to additional handling of special cases (e.g., division by zero).


.. code-block:: text

    module divider(
            input_a,
            input_b,
            input_a_stb,
            input_b_stb,
            output_z_ack,
            clk,
            rst,
            output_z,
            output_z_stb,
            input_a_ack,
            input_b_ack);


    input     clk;
    input     rst;        

    input     [31:0] input_a; 
    input     input_a_stb;     
    output    input_a_ack;

    input     [31:0] input_b;  
    input     input_b_stb; 
    output    input_b_ack;

    output    [31:0] output_z;
    output    output_z_stb;
    input     output_z_ack;   

In the code snippet above, we show the interface of the divider module of the FPU. The module takes two 32-bit floating-point inputs, `input_a` and `input_b`, along with their respective strobe signals. It produces a 32-bit output `output_z` along with its strobe signal. The module also includes clock and reset signals.

We are interested in verifying that the output strobe signal `output_z_stb` is produced in constant time after both input strobe signals `input_a_stb` and `input_b_stb` are acknowledged, regardless of the specific values of `input_a` and `input_b`.
The module also uses handshaking signals (`input_a_ack`, `input_b_ack`, and `output_z_ack`) to manage data flow and ensure proper synchronization between input and output operations.

Specifically, the one of the first violations found by HyperQB occur when the inputs to the divider are such that `input_b` is zero, leading to a longer execution time due to the special handling of division by zero cases.  Similar counterexamples exist for other special cases as defined in the snippet below.

.. code-block:: text

    special_cases:
      begin
        //if a is NaN or b is NaN return NaN 
        if ((a_e == 128 && a_m != 0) || (b_e == 128 && b_m != 0)) begin
          z[31] <= 1;
          z[30:23] <= 255;
          z[22] <= 1;
          z[21:0] <= 0;
          state_var <= put_z;
          //if a is inf and b is inf return NaN 
        end else if ((a_e == 128) && (b_e == 128)) begin
          z[31] <= 1;
          z[30:23] <= 255;
          z[22] <= 1;
          z[21:0] <= 0;
          state_var <= put_z;
        //if a is inf return inf
        end else if (a_e == 128) begin
          z[31] <= a_s ^ b_s;
          z[30:23] <= 255;
          z[22:0] <= 0;
          state_var <= put_z;
           //if b is zero return NaN
          if ($signed(b_e == -127) && (b_m == 0)) begin
            z[31] <= 1;
            z[30:23] <= 255;
            z[22] <= 1;
            z[21:0] <= 0;
            state_var <= put_z;
          end
        //if b is inf return zero
        end else if (b_e == 128) begin
          z[31] <= a_s ^ b_s;
          z[30:23] <= 0;
          z[22:0] <= 0;
          state_var <= put_z;
        //if a is zero return zero
        end else if (($signed(a_e) == -127) && (a_m == 0)) begin
          z[31] <= a_s ^ b_s;
          z[30:23] <= 0;
          z[22:0] <= 0;
          state_var <= put_z;
           //if b is zero return NaN
          if (($signed(b_e) == -127) && (b_m == 0)) begin
            z[31] <= 1;
            z[30:23] <= 255;
            z[22] <= 1;
            z[21:0] <= 0;
            state_var <= put_z;
          end
        //if b is zero return inf
        end else if (($signed(b_e) == -127) && (b_m == 0)) begin
          z[31] <= a_s ^ b_s;
          z[30:23] <= 255;
          z[22:0] <= 0;
          state_var <= put_z;
        end else begin
          //Denormalised Number
          if ($signed(a_e) == -127) begin
            a_e <= -126;
          end else begin
            a_m[23] <= 1;
          end
          //Denormalised Number
          if ($signed(b_e) == -127) begin
            b_e <= -126;
          end else begin
            b_m[23] <= 1;
          end
          state_var <= normalise_a;
        end
      end

Property
----------
As mentioned earlier, we want to verify that the FPU executes in constant time regardless of the input values. The HyperLTL formula expressing this property is as follows:

.. math::

    \forall \pi_A.\forall \pi_B.\ (\mathrm{rst}_{\pi_A} \land \mathrm{rst}_{\pi_B} \land \bigcirc\Box(\neg\mathrm{rst}_{\pi_A}  \land \neg \mathrm{rst}_{\pi_B})) \\ \rightarrow 
    \bigcirc\Box(\mathrm{input\_b\_stb}_{\pi_A} \land \mathrm{s\_input\_b\_ack}_{\pi_A} \land  \\ \mathrm{input\_b\_stb}_{\pi_B} \land \mathrm{s\_input\_b\_ack}_{\pi_B})  
    \\ \rightarrow \Box(\mathrm{s\_output\_b\_stb}_{\pi_A} \leftrightarrow \mathrm{s\_output\_b\_stb}_{\pi_B}).

In this formula, we quantify over two traces, :math:`\pi_A` and :math:`\pi_B`, representing two different executions of the FPU. The formula states that if both executions start in a reset state and then proceed without resets, and if both executions receive the same input strobe and acknowledgment signals for `input_b`, then the output strobe signals for `output_z` must occur simultaneously in both executions. This ensures that the timing of the output does not depend on the specific input values, thus verifying constant-time execution.