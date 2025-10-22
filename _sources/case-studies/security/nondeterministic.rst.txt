Nondeterministic Inputs and Transitions (NuSMV)
===============================================

Description of the Case Study
-----------------------------

To assess how nondeterminism affects non-interference verification, we extend the standard information-flow example by allowing
integer secrets and observables in the range :math:`0 \ldots k`. The first variant draws the secret nondeterministically at
initialisation, while the second keeps the initial secret fixed but introduces nondeterministic updates on the next transition.
HyperQB checks whether these variations still satisfy non-interference, using arithmetic comparisons rather than Boolean
equality. Exploring the search space reveals how additional nondeterminism impacts solver performance.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Case #14.1

        .. literalinclude :: ../benchmarks_ui/nusmv/security/ndet/NI_v2.smv
            :language: smv

    .. tab:: Case #14.2

        .. literalinclude :: ../benchmarks_ui/nusmv/security/ndet/NI_v3.smv
            :language: smv

The HyperLTL formula(s)
-----------------------

Both variants are analysed with the classic :math:`\forall\exists` non-interference property, adapted to compare integer values.
The existential trace must reproduce the public behaviour of the original run while allowing a different secret.

.. math::

   \varphi_{\text{NI}} =
   \forall \pi_A . \exists \pi_B .
   \Box \big(
      \mathit{low}_{\pi_A} = \mathit{low}_{\pi_B}
   \big)
   \land
   \Box \big(
      \mathit{high}_{\pi_A} \neq \mathit{high}_{\pi_B}
   \big)

.. tabs::

    .. tab:: Case #14.1 & #14.2

        .. literalinclude :: ../benchmarks_ui/nusmv/security/ndet/NI.hq
            :language: hq
