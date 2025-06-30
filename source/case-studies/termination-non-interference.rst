Termination-sensitive/-insensitive Non-interference
===================================================

Description of the Case Study
-----------------------------

It is a classic definition :ref:`[CS10] <CS10>` of whether leaking the information via termination channels is allowed, which derives
two notions of non-interference (NI). For *termination-insensitive*, if one trace terminates, then there must exists
another trace that either (1) terminates and obeys NI, or (2) not terminate. That is,

.. math::
    \varphi_{\text{tini}} = \forall \pi_A. \exists \pi_B. \Diamond(\mathit{halt}_{\pi_A}) \rightarrow
    \Box \left( \mathit{halt}_{\pi_B} \rightarrow
    \left( \left( \mathit{high}_{\pi_A} \neq \mathit{high}_{\pi_B} \right) \land
    \left( \mathit{low}_{\pi_A} = \mathit{low}_{\pi_B} \right) \right) \right)

*Termination-sensitive* strengthens the property by asking there must exists another trace that terminates *and* obeys
NI. We verify a program from :ref:`[UTK21] <UTK21>` with respect to termination sensitivity. By using *optimistic* semantics, both return
UNSAT, meaning no bugs can be found in the finite exploration. Hence, the program satisfies the properties

Benchmarks
---------

.. tabs::

    .. tab:: Case #10.1

        **The Model(s)**

        .. tabs::

            .. tab:: NI Example

                .. literalinclude :: models/10_NIexp/ni_example.smv
                    :language: smv

        **Formula**

        .. literalinclude :: models/10_NIexp/tini.hq
            :language: smv

    .. tab:: Case #10.2

        **The Model(s)**

        .. tabs::

            .. tab:: NI Example

                .. literalinclude :: models/10_NIexp/ni_example.smv
                    :language: smv

        **Formula**

        .. literalinclude :: models/10_NIexp/tsni.hq
            :language: smv