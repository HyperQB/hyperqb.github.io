Alternating Bit Protocol (NuSMV, w/loops)
=========================================

Description of the Case Study
-----------------------------

We study synthesis-by-scenarios for the Alternating Bit Protocol (ABP), a classic reliable-link protocol that tolerates message loss and duplication by tagging packets/acks with a single alternating bit. The setting contains two components **sender** and **receiver** whose actions are abstracted into a single control variable for each model: ``a_state`` for a *scenario* specification and ``b_state`` for a *synthesized* protocol candidate. The goal is **scenario conformance**: every finite or infinite trace that appears in one of the given scenarios must be simulated by some trace of the synthesized protocol.

We capture conformance via **SIMAE** (our simulation relation across executions) and a HyperLTL constraint :math:`\varphi_{\mathrm{conf}}` of the form :math:`\forall_{\text{small}}\,\exists_{\text{big}}`, reflecting that scenarios are much smaller than the actual protocol. We consider two synthesized protocols:

- a **correct** ABP that handles packet loss, and
- an **incorrect** ABP variant that cannot handle packet loss.

Using HyperQB, our procedure finds a SIMAE witness satisfying :math:`\varphi_{\mathrm{conf}}` for the correct ABP, and returns **UNSAT** for the incorrect one because the packet-loss scenario cannot be simulated by that protocol.
The NuSMV model(s)
------------------

.. tabs::

   .. tab:: ABP 1

      .. literalinclude:: ../benchmarks_ui/nusmv/loop_conditions/abp/abp_1.smv
         :language: smv

   .. tab:: ABP 2

      .. literalinclude:: ../benchmarks_ui/nusmv/loop_conditions/abp/abp_2.smv
         :language: smv

   .. tab:: ABP 2 buggy
      
      .. literalinclude:: ../benchmarks_ui/nusmv/loop_conditions/abp/abp_2_buggy.smv
         :language: smv

The HyperLTL formula(s)
-----------------------

The conformance constraint binds every scenario trace :math:`\pi_A` to *some* protocol trace :math:`\pi_B` whose abstract control agrees pointwise according to the scenario–protocol alignment. Intuitively, whenever the scenario is in a control macro-state (e.g., “initial”, “sent”, “ack-processing”), the protocol must be in the corresponding macro-state. We enforce this alignment globally with an invariant.

.. math::

   \begin{aligned}
   \varphi_{\text{conf}}
   \;=\;
   \forall \pi_A.\ \exists \pi_B.\ \mathbf{G}\Big(
     & (a\_state_{\pi_A}{=}1 \leftrightarrow b\_state_{\pi_B}{=}1) \ \land \\
     & (a\_state_{\pi_A}{=}2 \leftrightarrow b\_state_{\pi_B}{=}9) \ \land \\
     & (a\_state_{\pi_A}{=}3 \leftrightarrow b\_state_{\pi_B}{=}10) \ \land \\
     & ((a\_state_{\pi_A}{=}6 \lor a\_state_{\pi_A}{=}7) \leftrightarrow (b\_state_{\pi_B}{=}2 \lor b\_state_{\pi_B}{=}6)) \ \land \\
     & (a\_state_{\pi_A}{=}11 \leftrightarrow b\_state_{\pi_B}{=}8)
   \Big).
   \end{aligned}

.. tabs::

   .. tab:: Formula

      .. literalinclude:: ../benchmarks_ui/nusmv/loop_conditions/abp/abp.hq
         :language: hq

References
----------

.. _ABP3:

Alur, Rajeev; Martin, Milo; Raghothaman, Mukund; Stergiou, Christos; Tripakis, Stavros; and Udupa, Abhishek. “Synthesizing finite-state protocols from scenarios and requirements.” In *Haifa Verification Conference (HVC 2014)*, pp. 75–91. Springer, 2014.
