Co-termination (NuSMV)
======================

Description of the Case Study
-----------------------------

This property asks whether two different programs agree on termination, which can be formalized using a :math:`∀∀` HyperLTL formula:

.. math::

   \forall \pi_A.\forall \pi_B.\ \Diamond(\mathrm{term}_{\pi_A}) \leftrightarrow \Diamond(\mathrm{term}_{\pi_B}).

We consider two simple programs from :ref:`[UTK21] <co-termination-UTK21>`. In this case, depends on their initial conditions, the programs might either
diverge or agree on termination. Co-termination is a non-safety formula; however, our bounded semantics (in particular,
opt), is able to give a meaningful verdict even though this is not a finitely-refutable property.

Benchmarks
----------

.. tabs::

    .. tab:: Case #7.1

        **The Model(s)**

        .. tabs::

            .. tab:: Co-termination 1

                .. literalinclude :: ../benchmarks_ui/nusmv/security/coterm/coterm1.smv
                    :language: smv

            .. tab:: Co-termination 2

                .. literalinclude :: ../benchmarks_ui/nusmv/security/coterm/coterm2.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../benchmarks_ui/nusmv/security/coterm/coterm.hq
            :language: hq

References
----------

.. _co-termination-UTK21:

- [UTK21] `Hiroshi Unno, Tachio Terauchi, and Eric Koskinen. Constraint-based relational verification. In Computer Aided Verification: 33rd International Conference, CAV 2021, Virtual Event, July 20–23, 2021, Proceedings, Part I, pages 742–766. Springer, 2021. <https://doi.org/10.1007/978-3-030-81685-8_35>`_
