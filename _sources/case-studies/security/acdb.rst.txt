Access-Controlled Database: Observational Equivalence (NuSMV)
=============================================================

Description of the Case Study
-----------------------------

The access-controlled database (ACDB) benchmark models two processes that coordinate via locks to print records labelled
according to the current access level. Process ``proc1`` is authorised to produce entries ``A`` and ``B``; the second,
``proc2``, emits either ``C`` or ``D`` depending on whether the system is in high-security mode. We analyse the flattened
composition produced by asynchronous scheduling and require that observers cannot distinguish executions based solely on the
visible outputs. The HyperLTL property demands that for every trace there exists an observationally equivalent one, ensuring
that the print sequence never reveals the secret bit controlling the high-mode branch.

The NuSMV model(s)
------------------

``acdb_flattened.smv`` captures the composed system after encoding the scheduler, while ``acdb_composed.smv`` retains the modular
structure for reference. The benchmark instantiates the flattened variant for verification.

.. note::

   The flattened model omits the scheduling nondeterminism present in the composed description, enabling HyperQB to explore the
   reachable state space within the configured bound while preserving the observable traces.

.. tabs::

    .. tab:: Flattened ACDB

        .. literalinclude :: ../benchmarks_ui/nusmv/security/acdb/acdb_flattened.smv
            :language: smv

    .. tab:: Composed ACDB

        .. literalinclude :: ../benchmarks_ui/nusmv/security/acdb/acdb_composed.smv
            :language: smv

The HyperLTL formula(s)
-----------------------

The equivalence requirement states that every observable event emitted by ``proc1`` and ``proc2`` must match across the original
trace :math:`\pi_A` and the witness :math:`\pi_B` at each time instant :math:`t`. HyperQB solves the model under halting pessimistic
semantics, confirming that the database preserves confidentiality with respect to the four published outputs.

.. math::

   \varphi_{\text{ACDB}} =
   \forall \pi_A . \exists \pi_B . \exists t .
   \Box\Big(
      obs\_printA_{\pi_A}[t] = obs\_printA_{\pi_B}[t] \land
      obs\_printB_{\pi_A}[t] = obs\_printB_{\pi_B}[t] \land
      obs\_printC_{\pi_A}[t] = obs\_printC_{\pi_B}[t] \land
      obs\_printD_{\pi_A}[t] = obs\_printD_{\pi_B}[t]
   \Big)

.. tabs::

    .. tab:: ACDB Equivalence

        .. literalinclude :: ../benchmarks_ui/nusmv/security/acdb/acdb.hq
            :language: hq
