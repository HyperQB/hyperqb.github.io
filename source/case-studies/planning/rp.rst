Robust Path Planning (NuSMV)
===========================

Description of the Case Study
-----------------------------

We study **robust path planning (RP)** on a grid world, following . An **agent** must travel from a start cell to a goal cell while a set of **adversaries** moves under constrained dynamics (e.g., only clockwise). A path is *robust* if the agent can complete the mission **regardless of how the adversaries move** within their constraints.

This benchmark fits an :math:`\exists_{\text{agent}}\,\forall_{\text{adv}}` setting: we search for one agent strategy such that **all** adversary behaviors fail to intercept it. Using HyperQB, we encode conformance as a SIMAE-style relation between an *agent trace* and an *adversary trace family* and check the HyperLTL condition below. We provide a satisfiable instance (a robust path exists) and an unsatisfiable one (no robust path).

The NuSMV model(s)
------------------

.. tabs::

   .. tab:: Agent / arena

      ..  literalinclude::   ../../benchmarks_ui/nusmv/loop_conditions/mm/mm2.smv
          :language: smv

   .. tab:: Adversaries — variant A

      ..  literalinclude::                        # set path
          :language: smv

   .. tab:: Adversaries — variant B

      ..  literalinclude::                        # set path
          :language: smv

The HyperLTL formula(s)
-----------------------

We require that the agent **never occupies the same cell** as the adversaries, for **all** adversary behaviors; optionally we can also require eventual reachability of the goal.


.. math::

   \begin{aligned}
   \varphi_{\mathrm{RP}}
   \;=\;
   \exists \pi_{\text{agent}}.\ \forall \pi_{\text{adv}}.\ 
   \mathbf{G}\,\big(\mathit{pos}_{\pi_{\text{agent}}} \neq \mathit{pos}_{\pi_{\text{adv}}}\big).
   \end{aligned}



.. tabs::

   .. tab:: Formula (HQ)

      ..  literalinclude::                        # set path
          :language: hq



References
----------

.. _RPP23:

Filiot, Emmanuel; Lagarde, Guillaume; Laroussinie, François; Markey, Nicolas; Raskin, Jean-François; and Sankur, Ocan. “Efficient Loop Conditions for Bounded Model Checking Hyperproperties.” *arXiv:2301.06209*, 2023.
