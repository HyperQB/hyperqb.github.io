Symmetry in the Bakery Algorithm
================================

Description of the Case Study
-----------------------------

Lamport’s Bakery algorithm is a mutual exclusion protocol
for concurrent processes. The symmetry property states that no specific process
is privileged in terms of a faster access to the critical section, which is a desirable
property because it implies that concrete process ids are not relevant for faster
accesses. Symmetry is a hyperproperty that can be expressed with different HyperLTL formulas

.. math::
    \varphi_{S1} = \forall \pi_A . \forall \pi_B . \left(
    \neg \mathsf{sym}(select_{\pi_A}, select_{\pi_B}) \lor
    \neg(pause_{\pi_A} = pause_{\pi_B})
    \right) \mathcal{R} \\
    \left(
     (pc(P_0)_{\pi_A} = pc(P_1)_{\pi_B}) \land
     (pc(P_1)_{\pi_A} = pc(P_0)_{\pi_B})
    \right)

.. math::

   \varphi_{S2} =\ & \forall \pi_A . \forall \pi_B . \big( \neg \mathsf{sym}(select_{\pi_A}, select_{\pi_B}) \lor
         \neg(pause_{\pi_A} = pause_{\pi_B}) \lor \\
   &\quad \neg(select_{\pi_A} < 3) \lor
         \neg(select_{\pi_B} < 3) \big) \ \mathcal{R} \\
   &\quad \big( (pc(P_0)_{\pi_A} = pc(P_1)_{\pi_B}) \land
          (pc(P_1)_{\pi_A} = pc(P_0)_{\pi_B}) \big)

.. math::

   \varphi_{S3} =\ & \forall \pi_A . \forall \pi_B . \big(\neg \mathsf{sym}(select_{\pi_A}, select_{\pi_B}) \lor
          \neg(pause_{\pi_A} = pause_{\pi_B}) \lor \\
   &\quad \neg(select_{\pi_A} < 3) \lor
          \neg(select_{\pi_B} < 3) \lor \\
   &\quad \neg \mathsf{sym}(sym\_break_{\pi_A}, sym\_break_{\pi_B}) \big)
          \ \mathcal{R} \\
   &\quad \big( (pc(P_0)_{\pi_A} = pc(P_1)_{\pi_B}) \land
           (pc(P_1)_{\pi_A} = pc(P_0)_{\pi_B}) \big)

.. math::

    \varphi_{\text{sym}_1} =\ & \forall \pi_A . \exists \pi_B . \Box \mathsf{sym}(select_{\pi_A}, select_{\pi_B})
    \land (pause_{\pi_A} = pause_{\pi_B}) \land \\
    &\quad (pc(P_0)_{\pi_A} = pc(P_1)_{\pi_B}) \land (pc(P_1)_{\pi_A} = pc(P_0)_{\pi_B})

.. math::

   \begin{aligned}
   \varphi_{\text{sym}_2} =\ & \forall \pi_A . \exists \pi_B . \Box \mathsf{sym}(select_{\pi_A}, select_{\pi_B}) \land (pause_{\pi_A} = pause_{\pi_B}) \land \\
   &\quad (select_{\pi_A} < 3) \land (select_{\pi_B} < 3) \land \\
   &\quad (pc(P_0)_{\pi_A} = pc(P_1)_{\pi_B}) \land (pc(P_1)_{\pi_A} = pc(P_0)_{\pi_B})
   \end{aligned}

In these formulas, each process :math:`P_{n}` has
a program counter :math:`pc(P_{n})`; select indicates which process is selected to process
next; :math:`\text{pause}` if both processes are not selected; :math:`\text{sym_break}` is which process is
selected after a tie; and sym(:math:`\text{select}\pi_{A}` , :math:`\text{select}\pi_{B}` ) indicates if two traces exchange
the process ids of which processes proceeds. The basic Bakery algorithm does
not satisfy symmetry (i.e. :math:`\varphi_{sym_{1}}`), because when two or more processes are trying
to enter the critical section with the same ticket number, the process with the
smaller process ID has priority and process ID is statically fixed attribute. HyperQB returns SAT using the :math:`\text{pessimistic}` semantics, indicating that there exists a
counterexample to symmetry in the form of a falsifying witness to :math:`\pi_{A}` in formula
:math:`\varphi_{sym_{1}}`. The tool returns an observable witness within finite bound using the the
pessimistic semantics. Therefore, we conclude that all future observations violate
the property

Benchmarks
----------


.. tabs::
    .. tab:: Case #1.1
        **The Model(s)**

        .. tabs::

            .. tab:: Bakery 3 Processes

                .. literalinclude :: ../models/1_bakery/bakery_3procs.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../models/1_bakery/bakery_phi_sym1_3proc.hq
            :language: hq

    .. tab:: Case #1.2
        **The Model(s)**

        .. tabs::

            .. tab:: Bakery 3 Processes

                .. literalinclude :: ../models/1_bakery/bakery_3procs.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../models/1_bakery/bakery_phi_sym2_3proc.hq
            :language: hq

    .. tab:: Case #1.3
        **The Model(s)**

        .. tabs::

            .. tab:: Bakery 5 Processes

                .. literalinclude :: ../models/1_bakery/bakery_5procs.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../models/1_bakery/bakery_phi_sym1_5proc.hq
            :language: hq

    .. tab:: Case #1.4
        **The Model(s)**

        .. tabs::

            .. tab:: Bakery 5 Processes

                .. literalinclude :: ../models/1_bakery/bakery_5procs.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../models/1_bakery/bakery_phi_sym2_5proc.hq
            :language: hq