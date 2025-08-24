Fairness in Non-Repudiation Protocols (NuSMV)
=============================================

Description of the Case Study
-----------------------------

A *non-repudiation* protocol ensures that a receiver obtains a receipt from the sender, called *non-repudiation of
origin* (*NRO*), and the sender ends up having an evidence, named *non-repudiation of receipt* (*NRR*), through a
trusted third party. A non-repudiation protocol is *fair* if both *NRR* and *NRO* are either both received or both not
received by the parties.

.. math::

   \varphi_{\text{fair}} = \exists \pi_A . \forall \pi_B .
   (\lozenge m_{\pi_A}) \land
   (\lozenge NRR_{\pi_A}) \land
   (\lozenge NRO_{\pi_A}) \land \\
   \big(
     (\Box \bigwedge_{\mathit{act} \in \mathit{Act}_P} act_{\pi_A} \leftrightarrow act_{\pi_B})
     \rightarrow
     ((\lozenge NRR_{\pi_B}) \leftrightarrow (\lozenge NRO_{\pi_B}))
   \big) \land \\
   \big(
     (\Box \bigwedge_{\mathit{act} \in \mathit{Act}_Q} \neg act_{\pi_A} \leftrightarrow act_{\pi_B})
     \rightarrow
     ((\lozenge NRR_{\pi_B}) \leftrightarrow (\lozenge NRO_{\pi_B}))
   \big)

We studied two different protocols from :ref:`[JMM11] <JMM11>`, namely, :math:`T_{\text{incorrect}}` that chooses not to send out *NRR*
after receiving *NRO*, and a correct implementation :math:`T_{\text{correct}}` which is fair. For
:math:`T_{\text{correct}}`, *HyperQB* returns UNSAT in the *halting optimistic* semantics which indicates that the
protocol satisfies fairness. For :math:`T_{\text{incorrect}}`, *HyperQB* returns SAT in the *halting pessimistic*
semantics which implies that fairness is violated.

Benchmarks
----------

.. tabs::

    .. tab:: Case #4.1

        **The Model(s)**

        .. tabs::

            .. tab:: NRP Incorrect

                .. literalinclude :: ../benchmarks_ui/nusmv/security/nrp/NRP_incorrect.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../benchmarks_ui/nusmv/security/nrp/NRP_formula.hq
            :language: hq

    .. tab:: Case #4.2

        **The Model(s)**

        .. tabs::

            .. tab:: NRP Correct

                .. literalinclude :: ../benchmarks_ui/nusmv/security/nrp/NRP_correct.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../benchmarks_ui/nusmv/security/nrp/NRP_formula.hq
            :language: hq

References
----------

.. _JMM11:

- [JMM11] `W. Jamroga, S. Mauw, and M. Melissen. Fairness in non-repudiation protocols. In Proceedings of the 7th International Workshop on Security and Trust Management (STM), volume 7170, pages 122–139. Springer, 2011. <https://doi.org/10.1007/978-3-642-29963-6_10>`_
