Intransitive Non-interference (NuSMV)
=====================================

Description of the Case Study
-----------------------------

:ref:`[RG99] <RG99>`. Intransitivity *down-grades* non-interference (NI) in the cases that the systems secure correct information flow
with a thirdparty. Formally, given three parties :math:`A`, :math:`B` and :math:`C`, while the flow :math:`A` to
:math:`C` is uncertain, intransitive NI permitted such flow if :math:`A \rightsquigarrow B \land B \rightsquigarrow C`,
then :math:`A \rightsquigarrow C`. In this case we investigate *a shared buffer model* :ref:`[WGW10] <WGW10>`, which contains a *secret*
(S) process, an *unclassified* (U) process, and a *scheduler* (sched). The main idea is to prevent U from gaining secret
information about S by speculating sched, but imposing that this potential flow is allowable via identical sched. That
is, if the two executions agree on sched, the flow from S to U is considered safe. We apply this concept together with
classic hyperproperties *observational determinism* (OD) and *non-interference* (NI), and wrote two variations that
consider intransitivity:

.. math::
    \varphi_{\text{OD}_{\text{intra}}} = \forall \pi_A. \forall \pi_B. \Box \left( in^{U}_{\pi_A} \leftrightarrow in^{U}_{\pi_B} \right) \rightarrow
    \left( \left( sched_{\pi_A} \leftrightarrow sched_{\pi_B} \right) \mathcal{R} \left( out^{U}_{\pi_A} \leftrightarrow out^{U}_{\pi_B} \right) \right)
.. math::
    \varphi_{\text{NI}_{\text{intra}}} = \forall \pi_A. \exists \pi_B. \Box \left( \left( in^{S}_{\pi_A} = \epsilon \right) \land
    \left( out^{U}_{\pi_A} \leftrightarrow out^{U}_{\pi_B} \right) \right) \lor
    \Box \left( sched_{\pi_A} \leftrightarrow sched_{\pi_B} \right)

Benchmarks
----------

.. tabs::

    .. tab:: Case #9.1

        **The Model(s)**

        .. tabs::

            .. tab:: Unscheduled Buffer

                .. literalinclude :: ../models/9_buffer/unscheduled_buffer.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../models/9_buffer/classic_OD.hq
            :language: smv

    .. tab:: Case #9.2

        **The Model(s)**

        .. tabs::

            .. tab:: Scheduled Buffer

                .. literalinclude :: ../models/9_buffer/scheduled_buffer.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../models/9_buffer/intrans_OD.hq
            :language: smv

    .. tab:: Case #9.3

        **The Model(s)**

        .. tabs::

            .. tab:: Scheduled Buffer

                .. literalinclude :: ../models/9_buffer/scheduled_buffer.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../models/9_buffer/intrans_GMNI.hq
            :language: smv

References
----------
.. _RG99:
- [RG99] `Andrew W Roscoe and Michael H Goldsmith. What is intransitive noninterference? In Proceedings of the 12th IEEE computer security foundations workshop, pages 228–238. IEEE, 1999. <https://doi.org/10.1109/CSFW.1999.779776>`_
.. _WGW10:
- [WGW10] `Michael W Whalen, David A Greve, and Lucas G Wagner. Model checking information flow. In Design and verification of microprocessor systems for high-assurance applications, pages 381–428. Springer, 2010. <https://doi.org/10.1007/978-1-4419-1539-9_13>`_
