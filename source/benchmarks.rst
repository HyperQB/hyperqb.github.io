Benchmarks
==========
Our evaluations include the following cases:

- :ref:`Case #1.1-#1.4: Symmetry in the Bakery Algorithm<symmetry>`
- :ref:`Case #2.1-#2.2: Linearizability in SNARK Algorithm<linearizability>`
- :ref:`Case #3.1-#3.2: Non-interference in Typed Multi-threaded Programs<non-interference>`
- :ref:`Case #4.1-#4.2: Fairness in Non-repudiation Protocols<fairness>`
- :ref:`Case #5.1-#5.2: Privacy-Preserving Path Synthesis for Robots<path-planning>`
- :ref:`Case #6.1: Mutant Synthesis for Mutation Testing<mutation>`
- :ref:`Case #7.1: Co-termination of multiple programs<co-termination>`
- :ref:`Case #8.1: Deniability<deniability>`
- :ref:`Case #9.1 - #9.3: Intransitive Non-interference<i-non-interference>`
- :ref:`Case #10.1 - #10.2: TINI and TSNI<t-non-interference>`
- :ref:`Case #11.1: K-safety<t-non-interference>`
- :ref:`Case #12.1-#12.2: MapSynth<secrecy>`
- :ref:`Case #13.1-#13.2: TeamLTL<teamltl>`
- :ref:`Case #14.1: Non-deterministic init<nondeterministic>`
- :ref:`Case #14.2: Non-deterministic trans<nondeterministic>`

Description of Case Studies
---------------------------

.. _symmetry:
Symmetry in the Bakery Algorithm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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

.. _linearizability:
Linearizability
^^^^^^^^^^^^^^^

The second study consists on verifying linearizability of the SNARK concurrent datatype :ref:`[DDG+04] <DDG+04>`. SNARK implements a
concurrent double-ended queue using double-compare-and-swap (DCAS) and a doubly linked-list. *Linearizability* :ref:`[HW90] <HW90>` is a
hyperproperty that requires that any *history* of execution of a concurrent data structure—where history is sequence of
*invocations* and *responses* by different threads—matches some sequential order of invocations and responses.

.. math::

   \varphi_{\text{lin}} = \forall \pi_A.\exists \pi_B.\ \Box\left( \mathit{history}_{\pi_A} \leftrightarrow \mathit{history}_{\pi_B} \right)

SNARK is known to have two linearizability bugs. With the use of *pessimistic semantics*, a witness of linearizability
violation of length :math:`k` is enough to infer that the given system does not satisfy the linearizability property.
*HyperQB* returns SAT identifying both bugs and producing two counterexamples. The bugs returned are consistent with the
ones reported in :ref:`[DDG+04] <DDG+04>`.

.. _non-interference:
Non-interference in multi-threaded programs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

.. _fairness:
Fairness in non-repudiation protocols
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

.. _path-planning:
Path planning for robots
^^^^^^^^^^^^^^^^^^^^^^^^

In this case study we use *HyperQB* beyond verification, to synthesize strategies for robotic planning :ref:`[NWP19] <NWP19>`. Here, we
focus on producing a strategy that satisfies control requirements for a robot to reach a goal in a grid. First, the
robot should take the *shortest path*, expressed as:

.. math::

   \varphi_{\text{sp}} = \exists \pi_A . \forall \pi_B . \left( \neg goal_{\pi_B} \ \mathcal{U} \ goal_{\pi_A} \right)

We also used *HyperQB* to solve the *path robustness* problem, meaning that starting from an arbitrary initial state, a
robot reaches the goal by following a single strategy, expressed as:

.. math::

   \varphi_{\text{rb}} = \exists \pi_A . \forall \pi_B . \left( strategy_{\pi_B} \leftrightarrow strategy_{\pi_A} \right) \ \mathcal{U} \ \left( goal_{\pi_A} \land goal_{\pi_B} \right)

*HyperQB* returns SAT for the grids of sizes up to :math:`60 \times 60`.

.. _mutation:
Mutation testing
^^^^^^^^^^^^^^^^

Another application of hyperproperties with quantifier
alternation is the efficient generation of test suites for mutation testing. We
22
borrow a model from :ref:`[FBW19] <FBW19>` and apply the original formula that describes a good
test mutant together with the model, expressed as:

.. math::

   \varphi_{\text{mut}} = \exists \pi_A . \forall \pi_B \left(
   mut_{\pi_A} \land \neg mut_{\pi_B} \right) \land
   \left(
     \left( in_{\pi_A} \leftrightarrow in_{\pi_B} \right) \
     \mathcal{U} \
     \left( out_{\pi_A} \not\leftrightarrow out_{\pi_B} \right)
   \right)

HyperQB returns SAT which implies the successful finding of a qualified mutant.

.. _co-termination:
Co-termination
^^^^^^^^^^^^^^

This property asks whether two different programs agree on termination, which can be formalized using a :math:`∀∀` HyperLTL formula:

.. math::

   \forall \pi_A.\forall \pi_B.\ \Diamond(\mathrm{term}_{\pi_A}) \leftrightarrow \Diamond(\mathrm{term}_{\pi_B}).

We consider two simple programs from :ref:`[UTK21] <UTK21>`. In this case, depends on their initial conditions, the programs might either
diverge or agree on termination. Co-termination is a non-safety formula; however, our bounded semantics (in particular,
opt), is able to give a meaningful verdict even though this is not a finitely-refutable property.

.. _deniability:
Deniability
^^^^^^^^^^^
:ref:`[SSS20] <SSS20>`. In a program, for every possible run :math:`\pi_{A}` (e.g., potentially being observed by an adversary), there must
exist :math:`2^N` different runs, such that each agrees on :math:`\pi_{A}` on the observable parts, but differ on secret values.
While deniability is usually an example of *quantitative hyperproperties* :ref:`[FHT18] <FHT18>`, here we demonstrate the case when the
parameter is :math:`N = 1`, that is, an :math:`∀∃∃` formula:

.. math::

    \varphi_{\text{den}} = \forall \pi_A. \exists \pi_B. \exists \pi_C. \Box \left(
      \left( \mathit{obs}_{\pi_A} \leftrightarrow \mathit{obs}_{\pi_B} \right)
      \land
      \left( \mathit{obs}_{\pi_A} \leftrightarrow \mathit{obs}_{\pi_C} \right)
      \land
      \left( \mathit{sec}_{\pi_B} \not\leftrightarrow \mathit{sec}_{\pi_C} \right)
    \right).


We evaluate this formula with an Wallet1 and Wallet2 models :ref:`[BKR09] <BKR09>` with a possible attack, where the attacker can speculate
the total amount of an account (:math:`sec`) by repeatedly withdrawing a fix amount (:math:`obs`). The UNSAT outcome for
bug-hunting by HyperQB gives a positive verdict (i.e., :math:`\mathcal{K} |=\varphi_{\text{den}}`)

.. _i-non-interference:
Intransitive Non-interference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
:ref:`[RG99] <RG99>`. Intransitivity *down-grades* non-interference (NI) in the cases that the systems secure correct information flow
with a thirdparty. Formally, given three parties :math:`A`, :math:`B` and :math:`C`, while the flow :math:`A` to
:math:`C` is uncertain, intransitive NI permitted such flow if :math:`A \rightsquigarrow B \land B \rightsquigarrow C`,
then :math:`A \rightsquigarrow C`. In this case we investigate *a shared buffer model* :ref:`[WGW10] <WGW10>`, which contains a *secret*
(S) process, an *unclassified* (U) process, and a *scheduler* (sched). The main idea is to prevent U from gaining secret
information about S by speculating sched, but imposing that this potential flow is allowable via identical sched. That
is, if the two executions agree on sched, the flow from S to U is considered safe. We apply this concept together with
classic hyperproperties *observational determinism* (OD) and *non-interference* (NI), and wrote two variations that
consider intransitivity:

.. math::
    \varphi_{\text{OD}_{\text{intra}}} = \forall \pi_A. \forall \pi_B. \Box \left( in^{U}_{\pi_A} \leftrightarrow in^{U}_{\pi_B} \right) \rightarrow
    \left( \left( sched_{\pi_A} \leftrightarrow sched_{\pi_B} \right) \mathcal{R} \left( out^{U}_{\pi_A} \leftrightarrow out^{U}_{\pi_B} \right) \right)
.. math::
    \varphi_{\text{NI}_{\text{intra}}} = \forall \pi_A. \exists \pi_B. \Box \left( \left( in^{S}_{\pi_A} = \epsilon \right) \land
    \left( out^{U}_{\pi_A} \leftrightarrow out^{U}_{\pi_B} \right) \right) \lor
    \Box \left( sched_{\pi_A} \leftrightarrow sched_{\pi_B} \right)

.. _t-non-interference:
Termination-sensitive/-insensitive Non-interference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It is a classic definition :ref:`[CS10] <CS10>` of whether leaking the information via termination channels is allowed, which derives
two notions of non-interference (NI). For *termination-insensitive*, if one trace terminates, then there must exists
another trace that either (1) terminates and obeys NI, or (2) not terminate. That is,

.. math::
    \varphi_{\text{tini}} = \forall \pi_A. \exists \pi_B. \Diamond(\mathit{halt}_{\pi_A}) \rightarrow
    \Box \left( \mathit{halt}_{\pi_B} \rightarrow
    \left( \left( \mathit{high}_{\pi_A} \neq \mathit{high}_{\pi_B} \right) \land
    \left( \mathit{low}_{\pi_A} = \mathit{low}_{\pi_B} \right) \right) \right)

*Termination-sensitive* strengthens the property by asking there must exists another trace that terminates *and* obeys
NI. We verify a program from :ref:`[UTK21] <UTK21>` with respect to termination sensitivity. By using *optimistic* semantics, both return
UNSAT, meaning no bugs can be found in the finite exploration. Hence, the program satisfies the properties

.. _secrecy:
Secrecy-preserving Refinement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

.. _teamltl:
LTL with Team Semantics
^^^^^^^^^^^^^^^^^^^^^^^
TeamLTL :ref:`[VHF+20] <VHF+20>` can be presented as HyperLTL formulas by avoiding explicit references to traces (details in :ref:`[VHF+20] <VHF+20>`). Since our focus
is on HyperLTL, we only borrow the example with team scenarios from :ref:`[VHF+20] <VHF+20>`.

Consider an unknown input that affects the system behavior. To specify that
executions either agree on :math:`a` or :math:`b` depending on the input, one can write the
following HyperLTL formula:

.. math::
    \varphi_{\text{team}} = \exists \pi_A. \exists \pi_B. \forall \pi. \Box
    \left( a_{\pi_A} \leftrightarrow a_{\pi} \right) \lor \left( b_{\pi_B} \leftrightarrow b_{\pi} \right).

Team scenarios as HyperQB is able to correctly verify and synthesize the two traces in the team (i.e., :math:`\pi_{A}`
and :math:`\pi_{B}`), correctly

.. _nondeterministic:
Nondeterministic Inputs and Transitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To evaluate how nondeterministic choices impact model checking performance, we extend a standard example in two ways.

We first change the high and low as
integers ranging :math:`0 \ldots k`. Next, the model of #14.1 set the initial condition nondeterministically as a number from :math:`0 \ldots k`. Another model in #14.2, instead,
have high initially as :math:`0`, but on the next transition, have high set to a number :math:`\le k`.

The HyperLTL formula used is the classic :math:`\forall\exists` non-interference, but with arithmetic comparison instead of simply Boolean matching.

References
^^^^^^^^^^

1. `HyperQB: A QBF-Based Bounded Model Checker for Hyperproperties <https://arxiv.org/pdf/2109.12989>`_ *Tzu-Han Hsu, Borzoo Bonakdarpour, and César Sánchez*