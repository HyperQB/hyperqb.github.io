Declassification by Enforcement: Refinement Check (NuSMV)
=========================================================

Description of the Case Study
-----------------------------

Declassification by enforcement (DBE) compares a source program that conditionally releases secret data with a target program
that suppresses the public leak. The source executes a branch that writes the secret input to a public channel when a predicate
fails; otherwise, the secret is emitted on a protected channel. The target program always writes to the secret channel. The
refinement objective is to show that every public trace produced by the source also arises in the target, guaranteeing that the
declassification policy is satisfied.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Source program

        .. literalinclude :: ../benchmarks_ui/nusmv/security/dbe/DBE_source.smv
            :language: smv

    .. tab:: Target program

        .. literalinclude :: ../benchmarks_ui/nusmv/security/dbe/DBE_target.smv
            :language: smv

The HyperLTL formula
--------------------

The refinement property universally quantifies over two source traces and demands a witness that matches their public outputs at
every time instant. Because the target traces suppress public emissions, the formula ensures that any observable behaviour in
the source is replicable without revealing new secrets.

.. math::

   \begin{aligned}
   \varphi_{\text{DBE}} = {} & \forall \pi_A . \forall \pi_B . \exists \pi_C . \\
   & \Box\Big(
        out\_public_{\pi_A} = out\_public_{\pi_C}
        \land
        out\_public_{\pi_B} = out\_public_{\pi_C}
     \Big)
   \end{aligned}

.. tabs::

    .. tab:: Public Equivalence

        .. literalinclude :: ../benchmarks_ui/nusmv/security/dbe/DBE.hq
            :language: hq
