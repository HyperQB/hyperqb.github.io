Intransitive Non-interference (NuSMV)
=====================================

Description of the Case Study
-----------------------------

Intransitive non-interference :ref:`[RG99] <RG99>` relaxes classic information-flow guarantees by allowing certain flows only when an
intermediary participates. We study the shared buffer model of Whalen, Greve, and Wagner :ref:`[WGW10] <WGW10>`, featuring a secret process
(S), an unclassified process (U), and a scheduler (sched). The scheduler can legitimately relay information from S to U, so
observations are considered secure provided two runs use identical scheduling choices. HyperQB evaluates both observational
determinism and Goguen–Meseguer non-interference under this intransitive policy, comparing scenarios with and without explicit
scheduling control.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Case #9.1

        .. literalinclude :: ../benchmarks_ui/nusmv/security/buffer/unscheduled_buffer.smv
            :language: smv

    .. tab:: Case #9.2

        .. literalinclude :: ../benchmarks_ui/nusmv/security/buffer/scheduled_buffer.smv
            :language: smv

    .. tab:: Case #9.3

        .. literalinclude :: ../benchmarks_ui/nusmv/security/buffer/scheduled_buffer.smv
            :language: smv

The HyperLTL formula(s)
-----------------------

Two HyperLTL specifications capture the intransitive variants. The first adapts observational determinism, requiring equal
outputs for U whenever both runs observe the same inputs and scheduler decisions. The second expresses intransitive
non-interference, insisting that either the secret input is absent or scheduling remains identical across traces.

.. math::

   \varphi_{\text{OD}_{\text{intra}}} =
   \forall \pi_A . \forall \pi_B .
   \Box \left( in^{U}_{\pi_A} \leftrightarrow in^{U}_{\pi_B} \right)
   \rightarrow
   \left( \left( sched_{\pi_A} \leftrightarrow sched_{\pi_B} \right)
          \mathcal{R}
          \left( out^{U}_{\pi_A} \leftrightarrow out^{U}_{\pi_B} \right) \right)

.. math::

   \varphi_{\text{NI}_{\text{intra}}} =
   \forall \pi_A . \exists \pi_B .
   \left(
      \Box \left(
         (in^{S}_{\pi_A} = \epsilon)
         \land (out^{U}_{\pi_A} \leftrightarrow out^{U}_{\pi_B})
      \right)
      \lor
      \Box \left( sched_{\pi_A} \leftrightarrow sched_{\pi_B} \right)
   \right)

.. tabs::

    .. tab:: Case #9.1

        .. literalinclude :: ../benchmarks_ui/nusmv/security/buffer/classic_OD.hq
            :language: hq

    .. tab:: Case #9.2

        .. literalinclude :: ../benchmarks_ui/nusmv/security/buffer/intrans_OD.hq
            :language: hq

    .. tab:: Case #9.3

        .. literalinclude :: ../benchmarks_ui/nusmv/security/buffer/intrans_GMNI.hq
            :language: hq

References
----------

.. _RG99:

- [RG99] `A. W. Roscoe and M. H. Goldsmith. What is intransitive noninterference? In *Computer Security Foundations Workshop*, pages 228–238, 1999. <https://doi.org/10.1109/CSFW.1999.779776>`_

.. _WGW10:

- [WGW10] `M. W. Whalen, D. A. Greve, and L. G. Wagner. Model checking information flow. In *Design and Verification of Microprocessor Systems for High-Assurance Applications*, pages 381–428, 2010. <https://doi.org/10.1007/978-1-4419-1539-9_13>`_
