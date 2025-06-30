Secrecy-preserving Refinement
=============================

Description of the Case Study
-----------------------------

Relating programs at different levels (e.g., high vs. low, abstract vs. concrete) is often involved in system design.
For example, *secure compilation* specifies that when the compiler transforms the code (e.g., for optimization
purposes), the compiled code should still satisfy the intended security property. For instance, to preserve the classic
:math:`\forall \exists` non-interference property during compilation, an :math:`\exists \forall \forall \exists \exists`
formula must be verified. That is, there exists a mapping :math:`M` that preserves NI from code :math:`A` to code
:math:`B`, as follows:

.. math::

   \Phi_{\text{NI--ABM}} =
   \exists \pi_M .
   \forall \pi_{A_1} . \forall \pi_{B_1} .
   \exists \pi_{A_2} . \exists \pi_{B_2} .
   \left( \varphi_{\mathit{map}_1} \rightarrow
   \left( \varphi_{\mathit{map}_2} \land \psi_{\text{NI}} \right) \right)

HyperQB is able to correctly synthesize a correct mapping (i.e., the leading :math:`\exists`) if one exists. Such a
formula with *multiple quantifier alternations* bumps up the complexity of model checking by one step in the polynomial
hierarchy compared to the original non-interference formula.

Benchmarks
----------

.. tabs::

    .. tab:: Case #12.1

        **The Model(s)**

        .. tabs::

            .. tab:: Mapping Synthesis MA

                .. literalinclude :: models/12_mapsynth/msynth_MA.smv
                    :language: smv

            .. tab:: Mapping Synthesis MB

                .. literalinclude :: models/12_mapsynth/msynth_MB.smv
                    :language: smv

            .. tab:: Mapping Synthesis MM

                .. literalinclude :: models/12_mapsynth/msynth_MM.smv
                    :language: smv

        **Formula**

        .. literalinclude :: models/12_mapsynth/msynth.hq
            :language: smv

    .. tab:: Case #12.2

        **The Model(s)**

        .. tabs::

            .. tab:: Mapping Synthesis MA

                .. literalinclude :: models/12_mapsynth/msynth2_MA.smv
                    :language: smv

            .. tab:: Mapping Synthesis MB

                .. literalinclude :: models/12_mapsynth/msynth2_MB.smv
                    :language: smv

            .. tab:: Mapping Synthesis MM

                .. literalinclude :: models/12_mapsynth/msynth2_MM.smv
                    :language: smv

        **Formula**

        .. literalinclude :: models/12_mapsynth/msynth2.hq
            :language: smv