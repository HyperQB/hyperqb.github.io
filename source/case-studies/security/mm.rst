Translation Validation: Matrix Multiplication (NuSMV)
===========================================================

Description of the Case Study
-----------------------------

We investigate a translation-validation benchmark for a C program that performs matrix multiplication (MM). When executed, the high-level C code is compiled into a low-level RTL (Register–Transfer Level) implementation that introduces explicit memory reads/writes. Specifications are triples :math:`\langle \mathit{Pre},\, \mathit{annot},\, \mathit{Post} \rangle`, where :math:`\mathit{Pre}` and :math:`\mathit{Post}` are assertions and :math:`\mathit{annot}` is a partial function from labels to assertions.

We capture conformance via **SIMAE** and a HyperLTL constraint :math:`\varphi_{\mathrm{conf}}`, proving that the translated code satisfies the same specification as the source. We consider two variants:

- a **correct** translation (expected **SAT**: a SIMAE witness exists), and
- an **incorrect** translation (expected **UNSAT**).

The NuSMV model(s)
------------------

.. tabs::

   .. tab:: C / RTL — correct

      .. literalinclude:: ../benchmarks_ui/nusmv/loop_conditions/mm/mm1.smv
         :language: smv

   .. tab:: C / RTL — incorrect

      .. literalinclude:: ../benchmarks_ui/nusmv/loop_conditions/mm/mm2_buggy.smv
         :language: smv

The HyperLTL formula(s)
-----------------------

The conformance constraint ties every source trace :math:`\pi_A` to *some* target trace :math:`\pi_B` such that their abstract control variable :math:`s` remains aligned at all steps.

.. math::

   \begin{aligned}
   \varphi_{\mathrm{conf}}
   \;=\;
   \forall \pi_A.\ \exists \pi_B.\ \mathbf{G}\big(s_{\pi_A} = s_{\pi_B}\big).
   \end{aligned}

.. tabs::

   .. tab:: Formula

      .. literalinclude:: ../benchmarks_ui/nusmv/loop_conditions/mm/mm.hq
         :language: hq

References
----------

.. _MM4:

Barthe, Gilles; Grégoire, Benjamin; Heraud, Sylvain; Kunz, César; and Pacalet, Anne. “Implementing a direct method for certificate translation.” In *International Conference on Formal Engineering Methods (ICFEM 2009)*, pp. 541–560. Springer, 2009.
