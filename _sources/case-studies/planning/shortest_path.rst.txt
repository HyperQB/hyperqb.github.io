Shortest Paths: Grid-World Planning (NuSMV)
===========================================

Description of the Case Study
-----------------------------

We use *HyperQB* to synthesise optimal strategies for a mobile robot navigating a grid world :ref:`[NWP19] <NWP19>`. The agent
starts in the lower-left corner and must reach the upper-right goal cell while avoiding unnecessary detours. The *shortest-path*
HyperLTL specification asks for a strategy whose execution reaches the goal no later than any competing run. HyperQB searches
for such a trace in grids up to :math:`60 \times 60` (3,600 cells) and returns SAT, yielding a controller that is globally
optimal with respect to the goal-reaching time.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Grid 10x10 (100 cells)

        .. literalinclude :: ../benchmarks_ui/nusmv/planning/shortest_path/robotic_sp_100.smv
            :language: smv

    .. tab:: Grid 20x20 (400 cells)

        .. literalinclude :: ../benchmarks_ui/nusmv/planning/shortest_path/robotic_sp_400.smv
            :language: smv

    .. tab:: Grid 40x40 (1,600 cells)

        .. literalinclude :: ../benchmarks_ui/nusmv/planning/shortest_path/robotic_sp_1600.smv
            :language: smv

    .. tab:: Grid 60x60 (3,600 cells)

        .. literalinclude :: ../benchmarks_ui/nusmv/planning/shortest_path/robotic_sp_3600.smv
            :language: smv

The HyperLTL formula(s)
-----------------------

The shortest-path requirement states that there exists a trace :math:`\pi_A` whose goal is reached before any alternative trace
:math:`\pi_B`. Until :math:`\pi_A` visits the goal, :math:`\pi_B` must remain in non-goal states, ensuring that :math:`\pi_A`
arrives at the goal in the minimal number of steps.

.. math::

   \varphi_{\text{sp}} = \exists \pi_A . \forall \pi_B .
   \big( \neg\, goal_{\pi_B} \ \mathcal{U} \ goal_{\pi_A} \big)

.. tabs::

    .. tab:: Shortest Path

        .. literalinclude :: ../benchmarks_ui/nusmv/planning/shortest_path/robotic_sp_formula.hq
            :language: hq

References
----------

.. _NWP19:

- [NWP19] `S. Nalluri, Y. Wang, and M. Pajic. Hyperproperties for robotics: Planning via HyperLTL. In International Conference on Robotics and Automation (ICRA), pages 8011–8017, 2019. <https://doi.org/10.48550/arXiv.1911.11870>`_
