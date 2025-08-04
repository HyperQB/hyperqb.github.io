LTL with Team Semantics
=======================

Description of the Case Study
-----------------------------

TeamLTL :ref:`[VHF+20] <VHF+20>` can be presented as HyperLTL formulas by avoiding explicit references to traces (details in :ref:`[VHF+20] <VHF+20>`). Since our focus
is on HyperLTL, we only borrow the example with team scenarios from :ref:`[VHF+20] <VHF+20>`.

Consider an unknown input that affects the system behavior. To specify that
executions either agree on :math:`a` or :math:`b` depending on the input, one can write the
following HyperLTL formula:

.. math::
    \varphi_{\text{team}} = \exists \pi_A. \exists \pi_B. \forall \pi. \Box
    \left( a_{\pi_A} \leftrightarrow a_{\pi} \right) \lor \left( b_{\pi_B} \leftrightarrow b_{\pi} \right).

Team scenarios as HyperQB is able to correctly verify and synthesize the two traces in the team (i.e., :math:`\pi_{A}`
and :math:`\pi_{B}`), correctly

Benchmarks
----------

.. tabs::

    .. tab:: Case #13.1

        **The Model(s)**

        .. tabs::

            .. tab:: Team

                .. literalinclude :: ../models/13_teamltl/team.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../models/13_teamltl/team.hq
            :language: smv

    .. tab:: Case #13.2

        **The Model(s)**

        .. tabs::

            .. tab:: Team 2

                .. literalinclude :: ../models/13_teamltl/team2.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../models/13_teamltl/team.hq
            :language: smv

References
----------
.. _VHF+20:
- [VHF+20] `Jonni Virtema, Jana Hofmann, Bernd Finkbeiner, Juha Kontinen, and Fan Yang. Linear-time temporal logic with team semantics: Expressivity and complexity. arXiv preprint arXiv:2010.03311, 2020. <https://doi.org/10.48550/arXiv.2010.03311>`_
