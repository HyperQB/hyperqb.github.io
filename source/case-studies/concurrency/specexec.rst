Speculative Execution Defenses (NuSMV)
======================================

Description of the Case Study
-----------------------------

Speculative execution can transiently execute instructions whose effects should be discarded, potentially exposing secrets via
microarchitectural channels. The benchmark suite models seven optimisation stages, each provided with a non-speculative (``_nse``)
and speculative (``_se``) version. The systems consist of two cooperating processes that manipulate shared arrays and update a
public register ``var_Y``. The HyperLTL property demands that the public output remains zero even when speculation occurs,
capturing the absence of observable leakage.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Version 1

        .. tabs::

            .. tab:: Non-speculative

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/specexec/v1_nse.smv
                    :language: smv

            .. tab:: Speculative

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/specexec/v1_se.smv
                    :language: smv

    .. tab:: Version 2

        .. tabs::

            .. tab:: Non-speculative

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/specexec/v2_nse.smv
                    :language: smv

            .. tab:: Speculative

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/specexec/v2_se.smv
                    :language: smv

    .. tab:: Version 3

        .. tabs::

            .. tab:: Non-speculative

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/specexec/v3_nse.smv
                    :language: smv

            .. tab:: Speculative

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/specexec/v3_se.smv
                    :language: smv

    .. tab:: Version 4

        .. tabs::

            .. tab:: Non-speculative

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/specexec/v4_nse.smv
                    :language: smv

            .. tab:: Speculative

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/specexec/v4_se.smv
                    :language: smv

    .. tab:: Version 5

        .. tabs::

            .. tab:: Non-speculative

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/specexec/v5_nse.smv
                    :language: smv

            .. tab:: Speculative

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/specexec/v5_se.smv
                    :language: smv

    .. tab:: Version 6

        .. tabs::

            .. tab:: Non-speculative

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/specexec/v6_nse.smv
                    :language: smv

            .. tab:: Speculative

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/specexec/v6_se.smv
                    :language: smv

    .. tab:: Version 7

        .. tabs::

            .. tab:: Non-speculative

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/specexec/v7_nse.smv
                    :language: smv

            .. tab:: Speculative

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/specexec/v7_se.smv
                    :language: smv

The HyperLTL formula
--------------------

The property asserts that for every trace there exists a witness whose public output ``var_Y`` stays at zero in lockstep. All
secure non-speculative variants satisfy the property, while speculative versions that leak data violate it.

.. math::

   \begin{aligned}
   \varphi_{\text{se}} = {} & \forall \pi_A . \exists \pi_B . \exists t . \\
   & \Box\big( var\_Y_{\pi_A}[t] = 0 \land var\_Y_{\pi_B}[t] = 0 \big)
   \end{aligned}

.. tabs::

    .. tab:: Speculative Safety

        .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/specexec/se_prop.hq
            :language: hq
