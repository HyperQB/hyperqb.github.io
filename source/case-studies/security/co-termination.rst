Co-termination (NuSMV)
======================

Description of the Case Study
-----------------------------

Co-termination asks whether two programs always agree on termination behaviour. Following Unno, Terauchi, and Koskinen
:ref:`[UTK21] <co-termination-UTK21>`, we model two simple programs whose execution may diverge or terminate depending on their initial
states. HyperQB evaluates paired runs of these programs: if one program terminates under a given initial condition, the other
must terminate as well. Although co-termination is not a safety property, the tool’s optimistic bounded semantics can still
confirm agreement (UNSAT) or expose a mismatch (SAT) in bounded traces.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Case #7.1

        .. tabs::

            .. tab:: Program 1

                .. literalinclude :: ../benchmarks_ui/nusmv/security/coterm/coterm1.smv
                    :language: smv

            .. tab:: Program 2

                .. literalinclude :: ../benchmarks_ui/nusmv/security/coterm/coterm2.smv
                    :language: smv

The HyperLTL formula(s)
-----------------------

The property enforces that every pair of executions eventually reaches termination together. HyperQB checks the relational
HyperLTL specification below; any counterexample contains two traces whose termination behaviours diverge.

.. math::

   \varphi_{\text{coterm}} =
   \forall \pi_A . \forall \pi_B .
   \left( \Diamond \mathrm{term}_{\pi_A} \leftrightarrow \Diamond \mathrm{term}_{\pi_B} \right)

.. tabs::

    .. tab:: Case #7.1

        .. literalinclude :: ../benchmarks_ui/nusmv/security/coterm/coterm.hq
            :language: hq

References
----------

.. _co-termination-UTK21:

- [UTK21] `H. Unno, T. Terauchi, and E. Koskinen. Constraint-based relational verification. In *Computer Aided Verification (CAV)*, pages 742–766, 2021. <https://doi.org/10.1007/978-3-030-81685-8_35>`_
