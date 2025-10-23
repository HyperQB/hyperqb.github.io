Compiler Optimisations: Security-Preserving Refinement (NuSMV)
==============================================================

Description of the Case Study
-----------------------------

We study three compiler optimisation patterns and analyse whether they preserve the security guarantees of the original
program. Each optimisation transforms a loop-based routine into a more efficient variant: **Loop Peeling (LP)** moves one
iteration outside the loop, **Expression Folding Loop Peeling (EFLP)** normalises arithmetic expressions, and **Dead Branch
Elimination (DBE)** removes infeasible public branches. For every pair, the source model captures the original program and the
target model implements the optimised version. The HyperLTL specification requires that public outputs remain indistinguishable
across both programs, ensuring that the transformation does not introduce information leaks.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Loop Peeling — Source

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/LP_source.smv
            :language: smv

    .. tab:: Loop Peeling — Target

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/LP_target.smv
            :language: smv

    .. tab:: Expression Folding LP — Source

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/EFLP_source.smv
            :language: smv

    .. tab:: Expression Folding LP — Target

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/EFLP_target.smv
            :language: smv

    .. tab:: Dead Branch Elimination — Source

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/DBE_source.smv
            :language: smv

    .. tab:: Dead Branch Elimination — Target

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/DBE_target.smv
            :language: smv

The HyperLTL formula
--------------------

All three optimisations reuse the same observational determinism property: any two traces of the source must match the public
outputs of a witness trace, reflecting that the optimised program does not expose new public information.

.. math::

   \begin{aligned}
   \varphi_{\text{opt}} = {} & \forall \pi_A . \forall \pi_B . \exists \pi_C . \\
   & \Box\Big(
        out\_public_{\pi_A} = out\_public_{\pi_C}
        \land
        out\_public_{\pi_B} = out\_public_{\pi_C}
     \Big)
   \end{aligned}

.. tabs::

    .. tab:: Loop Peeling

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/LP.hq
            :language: hq

    .. tab:: Expression Folding LP

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/EFLP.hq
            :language: hq

    .. tab:: Dead Branch Elimination

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/DBE.hq
            :language: hq
