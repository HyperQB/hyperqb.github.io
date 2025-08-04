Path planning for robots (NuSMV)
================================

Description of the Case Study
-----------------------------

In this case study we use *HyperQB* beyond verification, to synthesize strategies for robotic planning :ref:`[NWP19] <NWP19>`. Here, we
focus on producing a strategy that satisfies control requirements for a robot to reach a goal in a grid. First, the
robot should take the *shortest path*, expressed as:

.. math::

   \varphi_{\text{sp}} = \exists \pi_A . \forall \pi_B . \left( \neg goal_{\pi_B} \ \mathcal{U} \ goal_{\pi_A} \right)

We also used *HyperQB* to solve the *path robustness* problem, meaning that starting from an arbitrary initial state, a
robot reaches the goal by following a single strategy, expressed as:

.. math::

   \varphi_{\text{rb}} = \exists \pi_A . \forall \pi_B . \left( strategy_{\pi_B} \leftrightarrow strategy_{\pi_A} \right) \ \mathcal{U} \ \left( goal_{\pi_A} \land goal_{\pi_B} \right)

*HyperQB* returns SAT for the grids of sizes up to :math:`60 \times 60`.

Benchmarks
----------

.. tabs::

    .. tab:: Case #5.1

        **The Model(s)**

        .. tabs::

            .. tab:: Robotic Robustness 100

                .. literalinclude :: ../models/5_planning/robotic_robustness_100.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../models/5_planning/robotic_robustness_formula.hq
            :language: smv

    .. tab:: Case #5.2

        **The Model(s)**

        .. tabs::

            .. tab:: Robotic Robustness 400

                .. literalinclude :: ../models/5_planning/robotic_robustness_400.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../models/5_planning/robotic_robustness_formula.hq
            :language: smv

    .. tab:: Case #5.3

        **The Model(s)**

        .. tabs::

            .. tab:: Robotic Robustness 1600

                .. literalinclude :: ../models/5_planning/robotic_robustness_1600.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../models/5_planning/robotic_robustness_formula.hq
            :language: smv

    .. tab:: Case #5.4

        **The Model(s)**

        .. tabs::

            .. tab:: Robotic Robustness 3600

                .. literalinclude :: ../models/5_planning/robotic_robustness_3600.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../models/5_planning/robotic_robustness_formula.hq
            :language: smv

References
----------
.. _NWP19:
- [NWP19] `S. Nalluri Y. Wang and M. Pajic. Hyperproperties for robotics: Planning via HyperLTL. In International Conference on Robotics and Automation (ICRA), pages 8011–8017, 2019 <https://doi.org/10.48550/arXiv.1911.11870>.`_
