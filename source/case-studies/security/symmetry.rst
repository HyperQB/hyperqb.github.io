Symmetry: Bakery Algorithm (NuSMV)
========================================

Description of the Case Study
-----------------------------

Lamport's Bakery algorithm :ref:`[Lam74] <Lam74>` is a classic first-come-first-served mutual exclusion protocol in which each
process draws a ticket and enters the critical section once it observes that it holds the smallest number. While safety and
liveness are guaranteed, the algorithm breaks ties using the intrinsic process identifier, potentially privileging lower-numbered
processes. We examine *symmetry*: if two executions differ only by swapping process identifiers, the resulting behaviour should
remain indistinguishable. The case study models configurations with 3, 7, 9, and 11 processes. HyperQB explores the reachable
state space under pessimistic semantics, so any bounded counterexample to symmetry generalises to an infinite execution that
demonstrates asymmetric access to the critical section.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: 3 processes

        .. literalinclude :: ../benchmarks_ui/nusmv/security/bakery/bakery3.smv
            :language: smv

    .. tab:: 7 processes

        .. literalinclude :: ../benchmarks_ui/nusmv/security/bakery/bakery7.smv
            :language: smv

    .. tab:: 9 processes

        .. literalinclude :: ../benchmarks_ui/nusmv/security/bakery/bakery9.smv
            :language: smv

    .. tab:: 11 processes

        .. literalinclude :: ../benchmarks_ui/nusmv/security/bakery/bakery11.smv
            :language: smv

The HyperLTL formula(s)
-----------------------

Symmetry can be expressed by relating pairs of traces that exchange process identifiers yet follow the same scheduling choices.
The formulas below progressively reinforce the equality constraints on ticket selection and tie-breaking. HyperQB reports SAT
for the standard Bakery implementation, producing witnesses that show how lower-numbered processes retain priority even when
tickets match.

.. math::

   \varphi_{S1} = \forall \pi_A . \forall \pi_B .
   \left(
      \neg \mathsf{sym}(select_{\pi_A}, select_{\pi_B})
      \lor \neg(pause_{\pi_A} = pause_{\pi_B})
   \right) \mathcal{R}
   \left(
      (pc(P_0)_{\pi_A} = pc(P_1)_{\pi_B})
      \land
      (pc(P_1)_{\pi_A} = pc(P_0)_{\pi_B})
   \right)

.. math::

   \varphi_{S2} = {} & \forall \pi_A . \forall \pi_B .
      \big(
         \neg \mathsf{sym}(select_{\pi_A}, select_{\pi_B})
         \lor \neg(pause_{\pi_A} = pause_{\pi_B})
         \lor \neg(select_{\pi_A} < 3)
         \lor \neg(select_{\pi_B} < 3)
      \big) \ \mathcal{R} \\
   & \big(
      (pc(P_0)_{\pi_A} = pc(P_1)_{\pi_B})
      \land
      (pc(P_1)_{\pi_A} = pc(P_0)_{\pi_B})
   \big)


.. math::

   \varphi_{S3} = {} & \forall \pi_A . \forall \pi_B .
      \big(
         \neg \mathsf{sym}(select_{\pi_A}, select_{\pi_B})
         \lor \neg(pause_{\pi_A} = pause_{\pi_B})
         \lor \neg(select_{\pi_A} < 3)
         \lor \neg(select_{\pi_B} < 3)
         \lor \neg \mathsf{sym}(sym\_break_{\pi_A}, sym\_break_{\pi_B})
      \big) \ \mathcal{R} \\
   & \big(
      (pc(P_0)_{\pi_A} = pc(P_1)_{\pi_B})
      \land
      (pc(P_1)_{\pi_A} = pc(P_0)_{\pi_B})
   \big)


.. math::

   \varphi_{\text{sym}_1} =
   \forall \pi_A . \exists \pi_B .
   \Box \Big(
      \mathsf{sym}(select_{\pi_A}, select_{\pi_B})
      \land (pause_{\pi_A} = pause_{\pi_B})
      \land (pc(P_0)_{\pi_A} = pc(P_1)_{\pi_B})
      \land (pc(P_1)_{\pi_A} = pc(P_0)_{\pi_B})
   \Big)

.. math::

   \varphi_{\text{sym}_2} = {} & \forall \pi_A . \exists \pi_B .
      \Box \Big(
         \mathsf{sym}(select_{\pi_A}, select_{\pi_B})
         \land (pause_{\pi_A} = pause_{\pi_B})
         \land (select_{\pi_A} < 3)
         \land (select_{\pi_B} < 3) \\
      & \qquad \land (pc(P_0)_{\pi_A} = pc(P_1)_{\pi_B})
         \land (pc(P_1)_{\pi_A} = pc(P_0)_{\pi_B})
      \Big)


The predicate :math:`sym(x_{\pi_A}, x_{\pi_B})` asserts that traces :math:`\pi_A` and :math:`\pi_B` coincide up to a swap of process
identifiers; ``select`` and ``pause`` capture the scheduler state; and ``sym_break`` records which process wins the tie after
equal tickets. The program counter :math:`pc(P_n)` tracks the stage of process :math:`P_n` in the Bakery protocol. Together these
constraints detect any trace where identifier swapping changes the observed behaviour.

.. tabs::

    .. tab:: Symmetry 3procs

        .. literalinclude :: ../benchmarks_ui/nusmv/security/bakery/symmetry.hq
            :language: hq

    .. tab:: Symmetry 7procs

        .. literalinclude :: ../benchmarks_ui/nusmv/security/bakery/symmetry7.hq
            :language: hq

    .. tab:: Symmetry 9procs

        .. literalinclude :: ../benchmarks_ui/nusmv/security/bakery/symmetry9.hq
            :language: hq

    .. tab:: Symmetry 11procs

        .. literalinclude :: ../benchmarks_ui/nusmv/security/bakery/symmetry11.hq
            :language: hq

References
----------

.. _Lam74:

- [Lam74] `L. Lamport. A new solution of Dijkstra's concurrent programming problem. Communications of the ACM, 17(8):453–455, 1974. <https://doi.org/10.1145/361082.361093>`_
