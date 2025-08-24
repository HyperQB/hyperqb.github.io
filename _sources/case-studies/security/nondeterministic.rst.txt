Nondeterministic Inputs and Transitions (NuSMV)
===============================================

Description of the Case Study
-----------------------------

To evaluate how nondeterministic choices impact model checking performance, we extend a standard example in two ways.

We first change the high and low as
integers ranging :math:`0 \ldots k`. Next, the model of #14.1 set the initial condition nondeterministically as a number from :math:`0 \ldots k`. Another model in #14.2, instead,
have high initially as :math:`0`, but on the next transition, have high set to a number :math:`\le k`.

The HyperLTL formula used is the classic :math:`\forall\exists` non-interference, but with arithmetic comparison instead of simply Boolean matching.

Benchmarks
----------

.. tabs::

    .. tab:: Case #14.1

        **The Model(s)**

        .. tabs::

            .. tab:: NI v2

                .. literalinclude :: ../benchmarks_ui/nusmv/security/ndet/NI_v2.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../benchmarks_ui/nusmv/security/ndet/NI.hq
            :language: smv

    .. tab:: Case #14.2

        **The Model(s)**

        .. tabs::

            .. tab:: NI v3

                .. literalinclude :: ../benchmarks_ui/nusmv/security/ndet/NI_v3.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../benchmarks_ui/nusmv/security/ndet/NI.hq
            :language: smv