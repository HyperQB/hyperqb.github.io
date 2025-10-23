Cache Timing Attack: Observational Determinism (NuSMV)
======================================================

Description of the Case Study
-----------------------------

The cache-attack benchmark models a three-stage protocol in which a victim process performs secret-dependent memory accesses,
while an attacker observes cache misses to infer the sensitive branch. We focus on the flattened NuSMV encoding that explicitly
unrolls the scheduler, counters, and control flow so every concrete interleaving is represented. The verification objective is
to establish observational determinism, guaranteeing that public cache observations do not reveal differences between the
high- and low-security inputs supplied to the protocol.

The NuSMV model
---------------

.. literalinclude:: ../benchmarks_ui/nusmv/security/cache_attack/cache_flattened.smv
   :language: smv

The HyperLTL formula
--------------------

The property compares executions that agree on both high and low inputs across all time instants. Whenever the precondition holds,
the observations ``PRINT_ONE`` and ``PRINT_ZERO``—representing cache-based outputs—must coincide for every timestamp, witnesses inclusive.

.. math::

   \begin{aligned}
   \varphi_{\text{OD}} = {} & \forall \pi_A . \exists \pi_B . \forall t_1 . \exists t_2 . \\
   & \Big(
         \Box\big(in\_HIGH_{\pi_A}[t_1] = in\_HIGH_{\pi_B}[t_1]\big)
         \land
         \Box\big(in\_LOW_{\pi_A}[t_1] = in\_LOW_{\pi_B}[t_1]\big)
     \Big) \\
   & \rightarrow
     \Box\Big(
         obs\_PRINT\_ONE_{\pi_A}[t_2] = obs\_PRINT\_ONE_{\pi_B}[t_2]
         \land
         obs\_PRINT\_ZERO_{\pi_A}[t_2] = obs\_PRINT\_ZERO_{\pi_B}[t_2]
     \Big)
   \end{aligned}

.. tabs::

    .. tab:: Observational Determinism

        .. literalinclude :: ../benchmarks_ui/nusmv/security/cache_attack/odnd.hq
            :language: hq
