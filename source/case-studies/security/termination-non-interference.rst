Termination-sensitive/-insensitive Non-interference (NuSMV)
===========================================================

Description of the Case Study
-----------------------------

Termination channels allow secrets to leak by influencing whether a program halts. Clarkson and Schneider :ref:`[CS10] <CS10>` distinguish
between termination-insensitive non-interference (TINI) and termination-sensitive non-interference (TSNI). We study the example
from Unno, Terauchi, and Koskinen :ref:`[UTK21] <UTK21>`, checking both notions with HyperQB. Under optimistic semantics the solver returns
UNSAT for both properties, indicating no finite counterexample exists—thus the program satisfies both TINI and TSNI.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Case #10.1

        .. literalinclude :: ../benchmarks_ui/nusmv/security/ni_exp/ni_example.smv
            :language: smv

    .. tab:: Case #10.2

        .. literalinclude :: ../benchmarks_ui/nusmv/security/ni_exp/ni_example.smv
            :language: smv

The HyperLTL formula(s)
-----------------------

The two properties differ in how they treat the halting trace. TINI allows the witness trace to diverge, while TSNI insists on
matching termination. HyperQB evaluates both specifications to confirm the absence of termination leaks.

.. math::

   \varphi_{\text{TINI}} =
   \forall \pi_A . \exists \pi_B .
   \Big(
      \Diamond \mathit{halt}_{\pi_A}
      \rightarrow
      \Box \big(
         \mathit{halt}_{\pi_B}
         \rightarrow
         (\mathit{high}_{\pi_A} \neq \mathit{high}_{\pi_B}
          \land \mathit{low}_{\pi_A} = \mathit{low}_{\pi_B})
      \big)
   \Big)

.. math::

   \varphi_{\text{TSNI}} =
   \forall \pi_A . \exists \pi_B .
   \Box \big(
      \mathit{halt}_{\pi_A}
      \leftrightarrow
      \mathit{halt}_{\pi_B}
   \big)
   \land
   \Box \big(
      \mathit{high}_{\pi_A} \neq \mathit{high}_{\pi_B}
      \rightarrow
      \mathit{low}_{\pi_A} = \mathit{low}_{\pi_B}
   \big)

.. tabs::

    .. tab:: Case #10.1

        .. literalinclude :: ../benchmarks_ui/nusmv/security/ni_exp/tini.hq
            :language: hq

    .. tab:: Case #10.2

        .. literalinclude :: ../benchmarks_ui/nusmv/security/ni_exp/tsni.hq
            :language: hq

References
----------

.. _CS10:

- [CS10] `M. R. Clarkson and F. B. Schneider. Hyperproperties. Journal of Computer Security, 18(6):1157–1210, 2010. <https://doi.org/10.3233/JCS-2009-0393>`_

.. _UTK21:

- [UTK21] `H. Unno, T. Terauchi, and E. Koskinen. Constraint-based relational verification. In *Computer Aided Verification (CAV)*, pages 742–766, 2021. <https://doi.org/10.1007/978-3-030-81685-8_35>`_
