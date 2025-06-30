Co-termination
==============

Description of the Case Study
-----------------------------

This property asks whether two different programs agree on termination, which can be formalized using a :math:`∀∀` HyperLTL formula:

.. math::

   \forall \pi_A.\forall \pi_B.\ \Diamond(\mathrm{term}_{\pi_A}) \leftrightarrow \Diamond(\mathrm{term}_{\pi_B}).

We consider two simple programs from :ref:`[UTK21] <UTK21>`. In this case, depends on their initial conditions, the programs might either
diverge or agree on termination. Co-termination is a non-safety formula; however, our bounded semantics (in particular,
opt), is able to give a meaningful verdict even though this is not a finitely-refutable property.

Benchmarks
---------

.. tabs::

    .. tab:: Case #7.1

        **The Model(s)**

        .. tabs::

            .. tab:: Co-termination 1

                .. literalinclude :: models/7_coterm/coterm1.smv
                    :language: smv

            .. tab:: Co-termination 2

                .. literalinclude :: models/7_coterm/coterm2.smv
                    :language: smv

        **Formula**

        .. literalinclude :: models/7_coterm/coterm.hq
            :language: smv