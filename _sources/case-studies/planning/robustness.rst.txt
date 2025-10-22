Path Robustness: Grid-World Planning (NuSMV)
============================================

Description of the Case Study
-----------------------------

Beyond optimality, we study *path robustness* for the same grid-world robot controller :ref:`[NWP19] <NWP19>`. The question is
whether a single strategy can guide the robot to the goal from any admissible initial configuration. The HyperLTL formulation
requires all runs that follow the synthesised strategy to synchronise on the same control choices, guaranteeing that every
starting state eventually reaches the goal under that policy. HyperQB establishes SAT for grids up to :math:`60 \times 60`,
showing that a uniform, robust controller exists even as the environment scales.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Grid 10x10 (100 cells)

        .. literalinclude :: ../benchmarks_ui/nusmv/planning/robotic_robustness/robotic_robustness_100.smv
            :language: smv

    .. tab:: Grid 20x20 (400 cells)

        .. literalinclude :: ../benchmarks_ui/nusmv/planning/robotic_robustness/robotic_robustness_400.smv
            :language: smv

    .. tab:: Grid 40x40 (1,600 cells)

        .. literalinclude :: ../benchmarks_ui/nusmv/planning/robotic_robustness/robotic_robustness_1600.smv
            :language: smv

    .. tab:: Grid 60x60 (3,600 cells)

        .. literalinclude :: ../benchmarks_ui/nusmv/planning/robotic_robustness/robotic_robustness_3600.smv
            :language: smv

The HyperLTL formula(s)
-----------------------

Path robustness is encoded by forcing any trace that mimics the chosen strategy to reach the goal in lockstep with the witness
trace. Once both executions are at the goal, the requirement is satisfied; until then they must agree on the control decisions.

.. math::

   \varphi_{\text{rb}} = \exists \pi_A . \forall \pi_B .
   \big( (strategy_{\pi_B} \leftrightarrow strategy_{\pi_A}) \ \mathcal{U} \ (goal_{\pi_A} \land goal_{\pi_B}) \big)

.. tabs::

    .. tab:: Path Robustness

        .. literalinclude :: ../benchmarks_ui/nusmv/planning/robotic_robustness/robotic_robustness_formula.hq
            :language: hq

References
----------

.. _NWP19:

- [NWP19] `S. Nalluri, Y. Wang, and M. Pajic. Hyperproperties for robotics: Planning via HyperLTL. In International Conference on Robotics and Automation (ICRA), pages 8011–8017, 2019. <https://doi.org/10.48550/arXiv.1911.11870>`_
