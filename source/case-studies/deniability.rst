Deniability
===========

Description of the Case Study
-----------------------------

:ref:`[SSS20] <SSS20>`. In a program, for every possible run :math:`\pi_{A}` (e.g., potentially being observed by an adversary), there must
exist :math:`2^N` different runs, such that each agrees on :math:`\pi_{A}` on the observable parts, but differ on secret values.
While deniability is usually an example of *quantitative hyperproperties* :ref:`[FHT18] <FHT18>`, here we demonstrate the case when the
parameter is :math:`N = 1`, that is, an :math:`∀∃∃` formula:

.. math::

    \varphi_{\text{den}} = \forall \pi_A. \exists \pi_B. \exists \pi_C. \Box \left(
      \left( \mathit{obs}_{\pi_A} \leftrightarrow \mathit{obs}_{\pi_B} \right)
      \land
      \left( \mathit{obs}_{\pi_A} \leftrightarrow \mathit{obs}_{\pi_C} \right)
      \land
      \left( \mathit{sec}_{\pi_B} \not\leftrightarrow \mathit{sec}_{\pi_C} \right)
    \right).


We evaluate this formula with an Wallet1 and Wallet2 models :ref:`[BKR09] <BKR09>` with a possible attack, where the attacker can speculate
the total amount of an account (:math:`sec`) by repeatedly withdrawing a fix amount (:math:`obs`). The UNSAT outcome for
bug-hunting by HyperQB gives a positive verdict (i.e., :math:`\mathcal{K} |=\varphi_{\text{den}}`)

Benchmarks
----------

.. tabs::

    .. tab:: Case #8.1

        **The Model(s)**

        .. tabs::

            .. tab:: Deniability Small

                .. literalinclude :: models/8_deniability/den_small.smv
                    :language: smv

        **Formula**

        .. literalinclude :: models/8_deniability/den_f1.hq
            :language: smv

    .. tab:: Case #8.2

        **The Model(s)**

        .. tabs::

            .. tab:: Deniability

                .. literalinclude :: models/8_deniability/den.smv
                    :language: smv

        **Formula**

        .. literalinclude :: models/8_deniability/den_f1.hq
            :language: smv
