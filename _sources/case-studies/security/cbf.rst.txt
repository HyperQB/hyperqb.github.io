Compiler Optimization: Common Branch Factorization (NuSMV, w/loops)
===================================================================

Description of the Case Study
-----------------------------

We study **compiler optimization** as preservation of input–output behaviors between a **source** program and an **optimized target** program. The case focuses on *common branch factorization (CBF)*: finding guards common to several if–then–else branches and hoisting them so the test is executed only once. While CBF reduces control complexity, it must not change observable behavior.

Conformance between source (big) and target (small) executions falls into the :math:`\forall_{\text{big}}\,\exists_{\text{small}}` category: for every source run there should exist a target run that matches the source’s observations. In our framework we avoid translating proofs and instead search for a **SIMAE** simulation that satisfies a conformance formula :math:`\varphi_{\mathrm{sc}}`.

We consider two targets:

- a **correct** optimization (expected **SAT**—a SIMAE witness exists), and
- a **buggy** optimization where some branches become unreachable (expected **UNSAT**).

The NuSMV model(s)
------------------

.. tabs::

   .. tab:: Source (big)

      .. literalinclude:: ../benchmarks_ui/nusmv/loop_conditions/cbf/cbf1.smv           
         :language: smv

   .. tab:: Target (small) — correct

      .. literalinclude:: ../benchmarks_ui/nusmv/loop_conditions/cbf/cbf2.smv
         :language: smv

   .. tab:: Target (small) — buggy

      .. literalinclude:: ../benchmarks_ui/nusmv/loop_conditions/cbf/cbf2_buggy.smv
         :language: smv

The HyperLTL formula(s)
-----------------------

We require that whenever the source and target agree on inputs, their observable outputs agree at all steps. With traces :math:`\pi_{\text{big}}` (source) and :math:`\pi_{\text{small}}` (target):

.. math::

   \begin{aligned}
   \varphi_{\mathrm{sc}}
   \;=\;
   \forall \pi_{\text{big}}.\ \exists \pi_{\text{small}}.\ 
   \big( \mathit{in}_{\pi_{\text{big}}} \leftrightarrow \mathit{in}_{\pi_{\text{small}}} \big)
   \ \rightarrow\
   \mathbf{G}\big( \mathit{out}_{\pi_{\text{big}}} \leftrightarrow \mathit{out}_{\pi_{\text{small}}} \big).
   \end{aligned}

.. tabs::

   .. tab:: Formula

      .. literalinclude::  ../benchmarks_ui/nusmv/loop_conditions/cbf/cbf.hq
         :language: hq



References
----------

.. _CBF32:

Namjoshi, Kedar S.; Tabajara, Lucas M. “Witnessing secure compilation.” In *International Conference on Verification, Model Checking, and Abstract Interpretation (VMCAI 2020)*, pp. 1–22. Springer, 2020.

