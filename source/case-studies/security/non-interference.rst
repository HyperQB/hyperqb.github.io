Non-interference: Multi-threaded Programs (NuSMV)
=================================================

Description of the Case Study
-----------------------------

Non-interference :ref:`[GM82] <GM82>` demands that changes to confidential inputs cannot be observed through public outputs.
We analyse the concurrent program introduced by Smith and Volpano :ref:`[SV98] <SV98>`, where the high-security input `PIN`
controls whether the low-security output `Result` reveals sensitive information. The benchmark includes both the original,
vulnerable implementation and the repaired version proposed in the paper. Using HyperQB under halting pessimistic semantics we
obtain a satisfying witness for the buggy program—demonstrating that two runs differing only in `PIN` can expose the secret via
`Result`. Switching to the fixed implementation and halting optimistic semantics, HyperQB proves unsatisfiability, confirming
that the repaired program enforces non-interference.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Case #3.1

        .. literalinclude :: ../benchmarks_ui/nusmv/security/ni/NI_incorrect.smv
            :language: smv

    .. tab:: Case #3.2

        .. literalinclude :: ../benchmarks_ui/nusmv/security/ni/NI_correct.smv
            :language: smv

The HyperLTL formula(s)
-----------------------

The property below captures termination-sensitive non-interference. Two executions must agree on the publicly observable output
`Result` whenever both runs terminate, even if they start with different secret inputs. The *until* operator constrains the
traces until simultaneous halting, ensuring observable equivalence once both executions finish.

.. math::

   \begin{aligned}
   \varphi_{\text{NI}} = {} & \forall \pi_A . \exists \pi_B .
      (\mathit{PIN}_{\pi_A} \neq \mathit{PIN}_{\pi_B}) \land \\
   & \big(
        (\neg \mathit{halt}_{\pi_A} \lor \neg \mathit{halt}_{\pi_B})
        \ \mathcal{U} \
        ((\mathit{halt}_{\pi_A} \land \mathit{halt}_{\pi_B})
         \land (\mathit{Result}_{\pi_A} = \mathit{Result}_{\pi_B}))
     \big)
   \end{aligned}

.. tabs::

    .. tab:: Case #3.1 & #3.2

        .. literalinclude :: ../benchmarks_ui/nusmv/security/ni/NI_formula.hq
            :language: hq

References
----------

.. _GM82:

- [GM82] `J. A. Goguen and J. Meseguer. Security policies and security models. In IEEE Symposium on Security and Privacy, pages 11–20, 1982. <https://doi.org/10.1109/SP.1982.10014>`_

.. _SV98:

- [SV98] `G. Smith and D. M. Volpano. Secure information flow in a multi-threaded imperative language. In Proceedings of the 25th ACM Symposium on Principles of Programming Languages (POPL), pages 355–364, 1998. <https://doi.org/10.1145/268946.268975>`_
