Generalized Non-interference: Banking Audit Logs (NuSMV)
=========================================================

Description of the Case Study
-----------------------------

Generalized non-interference :ref:`[GM82] <GM82>` requires that observables remain insensitive to confidential choices. We study
three NuSMV models of an online banking login workflow, each refining the instrumentation of the authentication stack. The
property of interest—*Always-Equivalent Evidence* (AEE)—states that, for any two executions, there must exist a third execution
whose return code matches one run while its audit trail mirrors the other. This captures the idea that public transaction logs
should not reveal which credentials were accepted. HyperQB, under halting pessimistic semantics, reports SAT for all three
models: the witness pairs a successful login trace with one that records a failed attempt. Because every version writes the
outcome directly into `loginfo`, no execution can combine the success code from one run with the failure log from another,
demonstrating a persistent violation of AEE even after successive simplifications of the system model.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Version 1 — Full instrumentation

        .. literalinclude :: ../benchmarks_ui/nusmv/security/bank/bank3_complex_V1.smv
            :language: smv

    .. tab:: Version 2 — Reduced environment

        .. literalinclude :: ../benchmarks_ui/nusmv/security/bank/bank3_complex_V2.smv
            :language: smv

    .. tab:: Version 3 — Minimal core

        .. literalinclude :: ../benchmarks_ui/nusmv/security/bank/bank3_complex_V3.smv
            :language: smv

The HyperLTL formula(s)
-----------------------

The AEE hyperproperty formalises the decoupling between observable results and audit evidence. For any traces :math:`\pi_A` and
:math:`\pi_B`, HyperQB must witness a third trace :math:`\pi_C` that always agrees with :math:`\pi_A` on the return code `result`
while reproducing the `loginfo` sequence of :math:`\pi_B`. If no such :math:`\pi_C` exists, the audit log leaks information about
which credentials succeeded.

.. math::

   \varphi_{\text{GMNI}} =
   \forall \pi_A . \forall \pi_B . \exists \pi_C .
   \Box(\mathit{result}_{\pi_A} = \mathit{result}_{\pi_C}) \land
   \Box(\mathit{loginfo}_{\pi_B} = \mathit{loginfo}_{\pi_C})

.. tabs::

    .. tab:: AEE

        .. literalinclude :: ../benchmarks_ui/nusmv/security/bank/gmni.hq
            :language: hq

References
----------

.. _GM82:

- [GM82] `J. A. Goguen and J. Meseguer. Security policies and security models. In IEEE Symposium on Security and Privacy, pages 11–20, 1982. <https://doi.org/10.1109/SP.1982.10014>`_
