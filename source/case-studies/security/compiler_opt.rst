Compiler Optimisations: Security-Preserving Refinement (NuSMV)
==============================================================

Description of the Case Study
-----------------------------

We study three compiler optimisation patterns and analyse whether they preserve the security guarantees of the original program. Each optimisation transforms a loop-based routine into a more efficient variant: **Loop Peeling (LP)** moves one iteration outside the loop, **Expression Folding Loop Peeling (EFLP)** normalises arithmetic expressions, and **Dead Branch
Elimination (DBE)** removes infeasible public branches. For every pair, the source model captures the original program and the target model implements the optimised version. The HyperLTL specification requires that public outputs remain indistinguishable across both programs, ensuring that the transformation does not introduce information leaks.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: LP Original — Source

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/original/lp/LP_source.smv
            :language: smv

    .. tab:: LP Original — Target

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/original/lp/LP_target.smv
            :language: smv

    .. tab:: LP Nondet — Source

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/with_ndet/lp/LP_source_ndet.smv
            :language: smv

    .. tab:: LP Nondet — Target

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/with_ndet/lp/LP_target_ndet.smv
            :language: smv

    .. tab:: LP Nondet — Incorrect Target

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/with_ndet/lp/LP_target_wrong_ndet.smv
            :language: smv

    .. tab:: LP Loop — Source

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/with_loops/lp/LP_source_ndet.smv
            :language: smv

    .. tab:: LP Loop — Target

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/with_loops/lp/LP_target_ndet.smv
            :language: smv
    
    .. tab:: LP Loop — Incorrect Target

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/with_loops/lp/LP_target_wrong_ndet.smv
            :language: smv

    .. tab:: EFLP — Source

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/original/eflp/EFLP_source.smv
            :language: smv

    .. tab:: EFLP — Target

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/original/eflp/EFLP_target.smv
            :language: smv

    .. tab:: EFLP Nondet — Source

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/with_ndet/eflp/EFLP_source_ndet.smv
            :language: smv

    .. tab:: EFLP Nondet — Target

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/with_ndet/eflp/EFLP_target_ndet.smv
            :language: smv

    .. tab:: DBE — Source

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/original/dbe/DBE_source.smv
            :language: smv

    .. tab:: DBE — Target

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/original/dbe/DBE_target.smv
            :language: smv

    .. tab:: DBE Nondet — Source

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/with_ndet/dbe/DBE_source_ndet.smv
            :language: smv

    .. tab:: DBE Nondet — Target

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/with_ndet/dbe/DBE_target_ndet.smv
            :language: smv
    
    .. tab:: DBE Nondet — Incorrect Target

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/with_ndet/dbe/DBE_wrong_ndet.smv
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

    .. tab:: LP

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/original/lp/LP.hq
            :language: hq

    .. tab:: LP Nondet

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/with_ndet/lp/LP.hq
            :language: hq

    .. tab:: LP Loops

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/with_loops/lp/LP.hq
            :language: hq

    .. tab:: LP Loops w/ Bug

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/with_loops/lp/LP.hq
            :language: hq

    .. tab:: EFLP

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/original/eflp/EFLP.hq
            :language: hq

    .. tab:: EFLP Nondet

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/with_ndet/eflp/EFLP.hq
            :language: hq

    .. tab:: DBE

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/original/dbe/DBE.hq
            :language: hq

    .. tab:: DBE Nondet

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/with_ndet/dbe/DBE.hq
            :language: hq

    .. tab:: DBE Nondet w/ Bug

        .. literalinclude :: ../benchmarks_ui/nusmv/security/compiler_opt/with_ndet/dbe/DBE.hq
            :language: hq
