Deniability (NuSMV)
===================

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

                .. literalinclude :: ../models/8_deniability/den_small.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../models/8_deniability/den_f1.hq
            :language: smv

    .. tab:: Case #8.2

        **The Model(s)**

        .. tabs::

            .. tab:: Deniability

                .. literalinclude :: ../models/8_deniability/den.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../models/8_deniability/den_f1.hq
            :language: smv

References
----------
.. _SSS20:
- [SSS20] `Shubham Sahai, Pramod Subramanyan, and Rohit Sinha. Verification of quantitative hyperproperties using trace enumeration relations. In Computer Aided Verification: 32nd International Conference, CAV 2020, Los Angeles, CA, USA, July 21–24, 2020, Proceedings, Part I 32, pages 201–224. Springer, 2020. <https://doi.org/10.48550/arXiv.2005.04606>`_
.. _FHT18:
- [FHT18] `Bernd Finkbeiner, Christopher Hahn, and Hazem Torfah. Model checking quantitative hyperproperties. In Computer Aided Verification: 30th International Conference, CAV 2018, Held as Part of the Federated Logic Conference, FloC 2018, Oxford, UK, July 14-17, 2018, Proceedings, Part I, pages 144–163. Springer, 2018. <https://doi.org/10.1007/978-3-319-96145-3_8>`_
.. _BKR09:
- [BKR09] `Michael Backes, Boris Köpf, and Andrey Rybalchenko. Automatic discovery and quantification of information leaks. In 2009 30th IEEE Symposium on Security and Privacy, pages 141–153. IEEE, 2009. <https://doi.org/10.1109/SP.2009.18>`_
