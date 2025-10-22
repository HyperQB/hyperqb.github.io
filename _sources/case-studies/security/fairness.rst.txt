Fairness: Non-Repudiation Protocols (NuSMV)
===========================================

Description of the Case Study
-----------------------------

Non-repudiation protocols aim to ensure that a sender cannot deny having sent a message (non-repudiation of origin, NRO) and
that a receiver cannot deny having received it (non-repudiation of receipt, NRR). Fairness requires that these evidences are
obtained symmetrically—either both parties possess their evidence or neither does. Following Jamroga, Mauw, and Melissen
:ref:`[JMM11] <JMM11>`, we model two variants: an incorrect protocol :math:`T_{\text{incorrect}}` that withholds the receipt after
obtaining NRO, and a corrected version :math:`T_{\text{correct}}`. When analysed with HyperQB, the faulty protocol yields a SAT
counterexample under halting pessimistic semantics, demonstrating unfair behaviour. The corrected protocol produces UNSAT
under halting optimistic semantics, confirming that it guarantees fairness.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Case #4.1

        .. literalinclude :: ../benchmarks_ui/nusmv/security/nrp/NRP_incorrect.smv
            :language: smv

    .. tab:: Case #4.2

        .. literalinclude :: ../benchmarks_ui/nusmv/security/nrp/NRP_correct.smv
            :language: smv

The HyperLTL formula(s)
-----------------------

Fairness is captured by a HyperLTL property requiring that whenever a cooperative environment delivers the same sequence of
actions for two traces, the availability of NRO and NRR must match. The existential trace chooses an execution where the sender
delivers the message and both evidences are eventually obtained; every trace that mirrors the sender or receiver schedules must
exhibit the same eventual outcomes.

.. math::

   \begin{aligned}
   \varphi_{\text{fair}} = {} & \exists \pi_A . \forall \pi_B .
      (\lozenge m_{\pi_A}) \land
      (\lozenge NRR_{\pi_A}) \land
      (\lozenge NRO_{\pi_A}) \land \\
   & \big(
      (\Box \bigwedge_{\mathit{act} \in \mathit{Act}_P} act_{\pi_A} \leftrightarrow act_{\pi_B})
      \rightarrow
      ((\lozenge NRR_{\pi_B}) \leftrightarrow (\lozenge NRO_{\pi_B}))
   \big) \land \\
   & \big(
      (\Box \bigwedge_{\mathit{act} \in \mathit{Act}_Q} \neg act_{\pi_A} \leftrightarrow act_{\pi_B})
      \rightarrow
      ((\lozenge NRR_{\pi_B}) \leftrightarrow (\lozenge NRO_{\pi_B}))
   \big)
   \end{aligned}

.. tabs::

    .. tab:: Case #4.1 & #4.2

        .. literalinclude :: ../benchmarks_ui/nusmv/security/nrp/NRP_formula.hq
            :language: hq

References
----------

.. _JMM11:

- [JMM11] `W. Jamroga, S. Mauw, and M. Melissen. Fairness in non-repudiation protocols. In Proceedings of the 7th International Workshop on Security and Trust Management (STM), volume 7170, pages 122–139. Springer, 2011. <https://doi.org/10.1007/978-3-642-29963-6_10>`_
