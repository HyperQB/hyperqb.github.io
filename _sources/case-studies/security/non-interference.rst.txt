Non-interference in multi-threaded programs (NuSMV)
===================================================

Description of the Case Study
-----------------------------

The hyperproperty of *non-interference* :ref:`[GM82] <GM82>` states that low-security variables are independent from the high-security
variables, thus preserving secure information flow. We consider the concurrent program example in :ref:`[SV98] <SV98>`, where `PIN` is
high security input and `Result` is low security output. *HyperQB* returns SAT in the *halting pessimistic* semantics,
indicating that there is a trace that we can spot the difference of high-variables by observing low variables, that is,
violating non-interference. With *HyperQB* we also verified the correctness of a fix to this algorithm, proposed in :ref:`[SV98] <SV98>`
as well. In this case, *HyperQB* uses the UNSAT results from the solver (with *halting optimistic* semantics) to infer
the absence of a violation.

.. math::

   \begin{aligned}
   \varphi_{\text{NI}} =\ & \forall \pi_A . \exists \pi_B . (\mathit{PIN}_{\pi_A} \neq \mathit{PIN}_{\pi_B}) \land \big( (\neg \mathit{halt}_{\pi_A} \lor \neg \mathit{halt}_{\pi_B})\ \mathcal{U} \\
   &\qquad ((\mathit{halt}_{\pi_A} \land \mathit{halt}_{\pi_B}) \land
            (\mathit{Result}_{\pi_A} = \mathit{Result}_{\pi_B})) \big)
   \end{aligned}

Benchmarks
----------

.. tabs::

    .. tab:: Case #3.1

        **The Model(s)**

        .. tabs::

            .. tab:: NI Incorrect

                .. literalinclude :: ../benchmarks_ui/nusmv/security/ni/NI_incorrect.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../benchmarks_ui/nusmv/security/ni/NI_formula.hq
            :language: smv

    .. tab:: Case #3.2

        **The Model(s)**

        .. tabs::

            .. tab:: NI Correct

                .. literalinclude :: ../benchmarks_ui/nusmv/security/ni/NI_correct.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../benchmarks_ui/nusmv/security/ni/NI_formula.hq
            :language: smv

References
----------
.. _GM82:
- [GM82] `J. A. Goguen and J. Meseguer. Security policies and security models. In IEEE Symp. on Security and Privacy, pages 11–20, 1982. <https://doi.org/10.1109/SP.1982.10014>`_
.. _SV98:
- [SV98] `G. Smith and D. M. Volpano. Secure information flow in a multi-threaded imperative language. In Proceedings of the 25th ACM Symposium on Principles of Programming Languages (POPL), pages 355–364, 1998. <https://doi.org/10.1145/268946.268975>`_
