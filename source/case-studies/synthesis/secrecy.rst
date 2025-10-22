Secrecy-preserving Refinement (NuSMV)
=============================

Description of the Case Study
-----------------------------

Relating programs at different levels (e.g., high vs. low, abstract vs. concrete) is often involved in system design.
For example, *secure compilation* specifies that when the compiler transforms the code (e.g., for optimization
purposes), the compiled code should still satisfy the intended security property. For instance, to preserve the classic
:math:`\forall \exists` non-interference property during compilation, an :math:`\exists \forall \forall \exists \exists`
formula must be verified. That is, there exists a mapping :math:`M` that preserves NI from code :math:`A` to code
:math:`B`.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: MapSynth 1

        .. tabs::

            .. tab:: Mapping Synthesis MA

                .. literalinclude :: ../benchmarks_ui/nusmv/synthesis/mapsynth/msynth_MA.smv
                    :language: smv

            .. tab:: Mapping Synthesis MB

                .. literalinclude :: ../benchmarks_ui/nusmv/synthesis/mapsynth/msynth_MB.smv
                    :language: smv

            .. tab:: Mapping Synthesis MM

                .. literalinclude :: ../benchmarks_ui/nusmv/synthesis/mapsynth/msynth_MM.smv
                    :language: smv

    .. tab:: MapSynth 2

        .. tabs::

            .. tab:: Mapping Synthesis MA

                .. literalinclude :: ../benchmarks_ui/nusmv/synthesis/mapsynth/msynth2_MA.smv
                    :language: smv

            .. tab:: Mapping Synthesis MB

                .. literalinclude :: ../benchmarks_ui/nusmv/synthesis/mapsynth/msynth2_MB.smv
                    :language: smv

            .. tab:: Mapping Synthesis MM

                .. literalinclude :: ../benchmarks_ui/nusmv/synthesis/mapsynth/msynth2_MM.smv
                    :language: smv

The HyperLTL formula(s)
-----------------------

The synthesis specification nests quantifiers to ensure that every abstract/concrete execution pair can be related by some
mapping trace :math:`\pi_M` that preserves non-interference. HyperQB searches for a witness mapping, increasing complexity by one
alternation over the underlying security requirement.

.. math::

   \Phi_{\text{NI--ABM}} =
   \exists \pi_M .
   \forall \pi_{A_1} . \forall \pi_{B_1} .
   \exists \pi_{A_2} . \exists \pi_{B_2} .
   \left( \varphi_{\mathit{map}_1} \rightarrow
   \left( \varphi_{\mathit{map}_2} \land \psi_{\text{NI}} \right) \right)

.. tabs::

    .. tab:: Case #12.1

        .. literalinclude :: ../benchmarks_ui/nusmv/synthesis/mapsynth/msynth.hq
            :language: hq

    .. tab:: Case #12.2

        .. literalinclude :: ../benchmarks_ui/nusmv/synthesis/mapsynth/msynth2.hq
            :language: hq
