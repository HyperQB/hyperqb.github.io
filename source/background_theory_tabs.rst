Background Theory
=================
.. tab-set::
   .. tab-item:: Theory (HLTL & A-HLTL)

      .. rubric:: HyperLTL (syntax and standard multi-trace semantics)

      We consider hyperproperties as formulas in **HyperLTL**, which extends LTL with explicit quantification over traces. The abstract syntax is

      .. math::

         \begin{array}{rcl}
         \varphi & ::= & \exists \pi \,.\, \varphi \mid \forall \pi \,.\, \varphi \mid \psi \\
         \psi    & ::= & \mathit{true} \mid a_\pi \mid \neg \psi \mid \psi \lor \psi \mid \psi \land \psi \mid \psi \,\mathcal{U}\, \psi \mid \psi \,\mathcal{R}\, \psi \mid \bigcirc \psi
         \end{array}

      Let a family of Kripke structures be :math:`\mathcal{K}=\langle K_\pi \rangle_{\pi\in \mathrm{Vars}(\varphi)}` and write :math:`T_\pi=\mathrm{Traces}(K_\pi)`. A (partial) **trace assignment** is a map :math:`\Pi:\mathrm{Vars}(\varphi)\rightharpoonup (2^{AP})^\omega`. Satisfaction (Boolean cases standard) is defined on pointed models :math:`(T,\Pi,i)` with :math:`i\in\mathbb{N}`:

      .. math::

         \begin{aligned}
         &(T,\Pi,0)\vDash \exists \pi.\,\phi &&\Leftrightarrow&& \exists t\in T_\pi:\ (T,\Pi[\pi\mapsto t],0)\vDash \phi,\\
         &(T,\Pi,0)\vDash \forall \pi.\,\phi &&\Leftrightarrow&& \forall t\in T_\pi:\ (T,\Pi[\pi\mapsto t],0)\vDash \phi,\\
         &(T,\Pi,i)\vDash a_\pi &&\Leftrightarrow&& a\in \Pi(\pi)(i),\\
         &(T,\Pi,i)\vDash \bigcirc \psi &&\Leftrightarrow&& (T,\Pi,i{+}1)\vDash \psi,\\
         &(T,\Pi,i)\vDash \psi_1\,\mathcal{U}\,\psi_2 &&\Leftrightarrow&& \exists j\ge i:\ (T,\Pi,j)\vDash \psi_2\ \land\ \forall k\in[i,j):\ (T,\Pi,k)\vDash \psi_1,\\
         &(T,\Pi,i)\vDash \psi_1\,\mathcal{R}\,\psi_2 &&\Leftrightarrow&& \Big(\forall j\ge i:\ (T,\Pi,j)\vDash \psi_2\Big)\ \text{or}\ \Big(\exists j\ge i:\ (T,\Pi,j)\vDash \psi_1 \land \forall k\in[i,j]:\ (T,\Pi,k)\vDash \psi_2\Big).
         \end{aligned}

      .. rubric:: Higher-order LTL (HLTL: syntax and semantics)

      **HLTL** generalizes HyperLTL by permitting variables that range over *tuples of traces* (arity :math:`d\ge 1`). This enables compact specifications of n-ary relations (e.g., 3-safety).

      Syntax extends atoms to point into a component of a tuple:

      .. math::

         \begin{array}{rcl}
         \varphi &::=& \exists \Pi.\,\varphi \mid \forall \Pi.\,\varphi \mid \psi,\\
         \psi &::=& \mathit{true} \mid a_{\Pi[j]} \mid \neg \psi \mid \psi \lor \psi \mid \psi \land \psi \mid \psi \,\mathcal{U}\, \psi \mid \psi \,\mathcal{R}\, \psi \mid \bigcirc \psi,
         \end{array}

      where :math:`\Pi` ranges over tuples :math:`((2^{AP})^\omega)^d` and :math:`j\in\{0,\dots,d-1\}`.

      A **tuple assignment** :math:`\Theta:\mathrm{Vars}(\varphi)\rightharpoonup ((2^{AP})^\omega)^d` maps each variable to a fixed-arity tuple of traces. Satisfaction extends the HyperLTL clauses; the atomic case becomes:

      .. math::

         (T,\Theta,i)\vDash a_{\Pi[j]} \ \Leftrightarrow\ a\in \Theta(\Pi)[j](i).

      (All Boolean/temporal operators and quantifiers behave as in HyperLTL, lifted through :math:`\Theta`.)

      .. rubric:: Asynchronous HyperLTL (A-HLTL: syntax and asynchronous semantics)

      **A-HLTL** augments HyperLTL with *trajectory quantifiers* that govern how traces progress relative to each other [2, 3]. In the BMC-oriented fragment (without next :math:`\bigcirc`):

      .. math::

         \begin{array}{rcl}
         \varphi &::=& \exists \pi.\,\varphi \mid \forall \pi.\,\varphi \mid E_\tau.\,\varphi \mid A_\tau.\,\varphi \mid \psi,\\
         \psi &::=& \mathit{true} \mid a_{\pi,\tau} \mid \neg \psi \mid \psi \lor \psi \mid \psi \land \psi \mid \psi \,\mathcal{U}\, \psi \mid \psi \,\mathcal{R}\, \psi.
         \end{array}

      A **trajectory** :math:`t` for the set of trace variables :math:`\mathrm{Paths}(\varphi)` is an :math:`\omega`-sequence :math:`t(0),t(1),\ldots` with :math:`t(i)\subseteq \mathrm{Paths}(\varphi)` indicating which traces advance at global step :math:`i` (others *stutter*). A trajectory is **fair** if every trace is selected infinitely often.

      We use a trajectory assignment :math:`\Gamma:\mathrm{Trajs}(\varphi)\rightharpoonup \mathrm{TRJ}` and an **asynchronous trace assignment** :math:`\Pi:\mathrm{Paths}(\varphi)\times \mathrm{Trajs}(\varphi)\to (2^{AP})^\omega\times \mathbb{N}` mapping :math:`(\pi,\tau)` to a pointed trace :math:`(\sigma,n)`. Define the successor :math:`\!(\Pi,\Gamma){+}1=(\Pi',\Gamma')\!` by incrementing :math:`n` exactly for those pairs with :math:`\pi\in \Gamma(\tau)(0)` and rotating the trajectories; write :math:`(\Pi,\Gamma){+}k` for the :math:`k`-fold iterate. Characteristic clauses (Boolean/quantifier cases as expected) are:

      .. math::

         \begin{aligned}
         &(\Pi,\Gamma)\vDash a_{\pi,\tau} &&\Leftrightarrow&& a\in \sigma(n)\ \text{ for }(\sigma,n)=\Pi(\pi,\tau),\\
         &(\Pi,\Gamma)\vDash \psi_1\,\mathcal{U}\,\psi_2 &&\Leftrightarrow&& \exists i\ge 0:\ (\Pi,\Gamma){+}i \vDash \psi_2\ \land\ \forall j<i:\ (\Pi,\Gamma){+}j \vDash \psi_1,\\
         &(\Pi,\Gamma)\vDash \psi_1\,\mathcal{R}\,\psi_2 &&\Leftrightarrow&& \forall i\ge 0:\ (\Pi,\Gamma){+}i \vDash \psi_2\ \text{or}\ \exists i\ge 0:\ (\Pi,\Gamma){+}i \vDash \psi_1 \land \forall j\le i:\ (\Pi,\Gamma){+}j \vDash \psi_2.
         \end{aligned}

      **Stutter-invariant fragment.** For bounded checking we restrict to formulas without :math:`\bigcirc`, so that inserted stuttering does not affect satisfaction; trajectories are assumed fair [2].

      .. rubric:: Worked example (HLTL vs A-HLTL)

      Property: *“Any two runs eventually produce the same output value, allowing different speeds.”*

      • **HLTL (synchronous)** (requires lockstep convergence):

      .. math::

         \forall \Pi.\ \Box\Diamond\big(out_{\Pi[0]} = out_{\Pi[1]}\big)
         \qquad\text{with arity } d{=}2.

      • **A-HLTL (asynchronous)** (allows stuttering/interleavings):

      .. math::

         \forall \pi_1.\forall \pi_2.\ A_\tau.\ \Box\Diamond\big(out_{\pi_1,\tau} = out_{\pi_2,\tau}\big).

      If one trace pauses while the other advances, A-HLTL still measures “eventually equal” along the fair trajectory, whereas HLTL demands equality along the *global* time axis.

   .. tab-item:: BMC Algorithm

      .. rubric:: Formal preliminaries

      A Kripke structure is :math:`K=\langle S,S_0,\delta,AP,L\rangle` with total transition relation :math:`\delta\subseteq S\times S` and labeling :math:`L:S\to 2^{AP}`. A path :math:`s(0)s(1)\ldots` induces a trace :math:`\sigma(i)=L(s(i))`. Write :math:`\mathrm{Traces}(K)` for all traces from :math:`S_0`.

      .. rubric:: 1) Unrolling models (bound :math:`k`)

      For each :math:`K_A`, introduce time-stamped copies :math:`x_A^0,\ldots,x_A^k`. With initial constraint :math:`I_A(x_A^0)` and step relation :math:`R_A(x_A^i,x_A^{i+1})`, define

      .. math::

         \text{⟦}K_A\text{⟧}_k \;=\; I_A(x_A^0)\ \land\ \bigwedge_{i=0}^{k-1} R_A(x_A^i,x_A^{i+1}).

      .. rubric:: 2) Encoding the temporal core (pess/opt/halting variants)

      Inductively encode subformulas :math:`\text{⟦}\psi\text{⟧}^{*}_{i,k}` with :math:`*\in\{\text{pes},\text{opt},\text{hpes},\text{hopt}\}`:

      .. math::

         \begin{aligned}
         &\text{⟦}p_\pi\text{⟧}^{*}_{i,k}=p_\pi^i,\quad &&\text{⟦}\neg p_\pi\text{⟧}^{*}_{i,k}=\neg p_\pi^i,\\
         &\text{⟦}\psi_1\lor \psi_2\text{⟧}^{*}_{i,k}=\text{⟦}\psi_1\text{⟧}^{*}_{i,k}\lor \text{⟦}\psi_2\text{⟧}^{*}_{i,k},\quad
         &&\text{⟦}\psi_1\land \psi_2\text{⟧}^{*}_{i,k}=\text{⟦}\psi_1\text{⟧}^{*}_{i,k}\land \text{⟦}\psi_2\text{⟧}^{*}_{i,k},\\
         &\text{⟦}\psi_1\,\mathcal{U}\,\psi_2\text{⟧}^{*}_{i,k}=\text{⟦}\psi_2\text{⟧}^{*}_{i,k}\lor\big(\text{⟦}\psi_1\text{⟧}^{*}_{i,k}\land \text{⟦}\psi_1\,\mathcal{U}\,\psi_2\text{⟧}^{*}_{i+1,k}\big),\\
         &\text{⟦}\psi_1\,\mathcal{R}\,\psi_2\text{⟧}^{*}_{i,k}=\text{⟦}\psi_2\text{⟧}^{*}_{i,k}\land\big(\text{⟦}\psi_1\text{⟧}^{*}_{i,k}\lor \text{⟦}\psi_1\,\mathcal{R}\,\psi_2\text{⟧}^{*}_{i+1,k}\big).
         \end{aligned}

      Base cases at :math:`k{+}1` select the bounded semantics [1, 2]:

      .. math::

         \begin{aligned}
         &\text{⟦}\psi\text{⟧}^{\text{pes}}_{k+1,k}=\mathit{false},\quad
         &&\text{⟦}\psi\text{⟧}^{\text{opt}}_{k+1,k}=\mathit{true},\\
         &\text{⟦}\psi\text{⟧}^{\text{hpes}}_{k+1,k}=\text{⟦}\mathsf{halted}\text{⟧}^{\text{hpes}}_{k,k}\land \text{⟦}\psi\text{⟧}^{\text{hpes}}_{k,k},\quad
         &&\text{⟦}\psi\text{⟧}^{\text{hopt}}_{k+1,k}=\text{⟦}\mathsf{halted}\text{⟧}^{\text{hopt}}_{k,k}\rightarrow \text{⟦}\psi\text{⟧}^{\text{hopt}}_{k,k}.
         \end{aligned}

      .. rubric:: 3) Bounded A-HLTL semantics (two bounds :math:`k\le m`)

      We bound **paths** by :math:`k` and **trajectories** by :math:`m` [2]. Let :math:`\mathrm{pos}_{\pi,\tau}(i)` count how many times :math:`\pi` has been selected in :math:`\tau(0),\ldots,\tau(i)`. Predicate :math:`\mathsf{off}` holds at :math:`(\Pi,\Gamma,i)` iff some selected pair :math:`(\pi,\tau)` has :math:`\mathrm{pos}_{\pi,\tau}(i)>k` before visiting a halting state. Temporal clauses follow the inductive rules above for :math:`i<m`; boundary behavior at :math:`i=m` is given by the halting pessimistic/optimistic variants (require vs. allow reading satisfaction at the boundary if :math:`\mathsf{halted}` holds).

      .. rubric:: 3′) Bounded HLTL semantics (synchronous tuples)

      For **HLTL**, tuple components advance **in lockstep**. On bound :math:`k`, satisfaction of :math:`\psi` at index 0 is exactly :math:`\text{⟦}\psi\text{⟧}^{*}_{0,k}` with atoms interpreted as :math:`a_{\Pi[j]}^i`. No trajectory bound is needed since there is no interleaving; halting variants (hpes/hopt) apply verbatim at :math:`k{+}1`.

      .. rubric:: 4) QBF compilation

      For :math:`\varphi=Q_A\,\pi_A.\cdots Q_Z\,\pi_Z.\,\psi` (stutter-invariant), associate each :math:`\pi_j` with :math:`K_j` and build

      .. math::

         \text{⟦}\mathcal{K},\varphi\text{⟧}^{*}_k \;=\; Q_A\,\overline{x_A}\cdot Q_B\,\overline{x_B}\cdots Q_Z\,\overline{x_Z}\;
         \Big(\text{⟦}K_A\text{⟧}_k\ \circ_A\ \cdots\ \circ_Z\ \text{⟦}\psi\text{⟧}^{*}_{0,k}\Big),
         \qquad
         \circ_j=\begin{cases}\wedge & Q_j=\exists,\\ \rightarrow & Q_j=\forall.\end{cases}

      The QBF’s satisfiability is equivalent to the bounded satisfaction of :math:`\varphi` (and is exact on terminating systems under halting variants) [1, 2].

   .. tab-item:: Intermediate Representation

      .. rubric:: Intermediate Representation
.. _common-section:

A key component of any `Bounded Model Checking`` (BMC) framework is the intermediate representation (IR) used to model the system under analysis. For this project, we developed an IR inspired by the NuSMV modeling language [1]_. It is designed to be **solver-agnostic** and captures the two essential components of a state machine: the state variables and the transition logic.

Suppose the set of transitions for a variable ``var`` is as follows:

.. code-block:: smv

    next(var) := case
        g1 : u1;
        g2 : u2;
        ...
        gk : uk;
        TRUE : u
    esac;

where ``next(var)`` specifies the value of ``var`` in the next state. In this format, each line ``g : u;`` is a guarded transition, consisting of a boolean condition ``g`` and an update expression ``u`` (which must match the variable's type).

We chose this model for its natural ability to clearly and independently define the transition logic for each state variable. This separation simplifies the analysis pipeline, as we can reason about transitions without concern for the concrete representation of a full state. In this model, a state is simply a valuation of all system variables. The core data structure implementing this IR in our code is ``SMVEnv``, which we refer to as the environment.

During a state change, the conditions are evaluated in order from top to bottom. The first condition ``g`` that holds determines the variable's next value via its corresponding update expression ``u``. If no condition holds, the ``TRUE`` branch is taken, which typically assigns the variable's current value (e.g., ``TRUE : variable;``), indicating a self-loop where no value change occurs.

The ``SMVEnv`` currently supports three variable types:

1. ``Boolean``: A boolean type, with an optional initial value.

2. ``Int``: A boundless mathematical integer, with optional initial, lower-bound, and upper-bound values.

3. ``BV``: A bit-vector type, which requires a bit-width. It can also have optional initial, lower-bound, and upper-bound values.

Defining States and Transitions
-------------------------------

Once an ``SMVEnv`` is created, new variables are added using the ``register_variable(name, type)`` method. All metadata (such as bounds or initial values) is specified within the ``type`` argument.

Transitions for a variable are defined using the ``register_transition(name, cond, upd)`` method. This method is called once for each guarded transition (like ``g: u;``) in the specific order they should be evaluated. The environment preserves this registration order, ensuring the priority logic of the NuSMV-style ``case`` statement is correctly modeled.

A key feature of our IR is that both the condition ``cond`` and the update expression ``upd`` are provided as native Rust functions. This allows for highly flexible and complex transition logic that can leverage the full power of the Rust language.

If no transitions are registered for a variable, the environment automatically assumes a self-loop (i.e., ``next(variable) := variable``).


Using Predicates
----------------

It is often necessary to check if a specific Boolean condition holds in a given state. Instead of rewriting this logic repeatedly, the IR allows you to define `predicates`.

A predicate is a named, reusable Rust boolean function that is evaluated against the current state. They are defined using the ``register_predicate(name, pred)`` method, where ``name`` is a string for future reference and pred is the boolean function. Predicates are useful for defining properties or checking for specific conditions, such as identifying a halting state in the system.

Translation to IR
-----------------

Our tool accepts two types of input files: **NuSMV** and **Verilog**.
We implement dedicated parsers for each language to translate the input into our intermediate representation (IR).
Once the IR is constructed, the remainder of the pipeline operates uniformly on it to generate either the QBF or SMT encoding.

Usage
----------
As an example, consider a simple system with a counter that iterates repeatedly from 0 to 15, and an LED that blinks every third cycle (i.e., when the counter is 0, 3, 6, 9, 12, or 15).

This system can be modeled in **NuSMV** as shown below:

.. code-block:: smv

    MODULE main
    VAR
    counter : 0..15;     -- 4-bit counter
    LED : boolean;   -- Denotes whether the LED is on

    DEFINE
    reset   := counter = 15;       -- predicate: counter about to reset
    led_blink:= (counter mod 3 = 2) | reset; -- true at counter = 2, 5, 8, 11, 14, 15

    ASSIGN
    init(counter) := 0;
    init(LED) := TRUE; -- Should blink counter = 0

    -- counter: 0..15 then reset to 0
    next(counter) := case
        reset : 0;
        TRUE : counter + 1;
    esac;

    -- Only blink if the led_blink is true
    next(LED) := case
        led_blink : TRUE;
        TRUE: FALSE;
    esac;

The corresponding **Verilog** implementation is presented below:

.. code-block:: verilog

    module counter_led (
        input  wire       clk,
        input  wire       rst_n,     // active-low reset
        output reg  [3:0] counter,
        output reg        LED
    );

        wire reset_pred = (counter == 4'd15);

        wire led_blink = (counter == 4'd2 ) |
                        (counter == 4'd5 ) |
                        (counter == 4'd8 ) |
                        (counter == 4'd11) |
                        (counter == 4'd14) |
                        reset_pred;

        always @(posedge clk or negedge rst_n) begin
            if (!rst_n) begin
                
                counter <= 4'd0;
                LED     <= 1'b1;
            end else begin
                
                counter <= reset_pred ? 4'd0 : (counter + 4'd1);
                LED     <= led_blink ? 1'b1 : 1'b0;
            end
        end

    endmodule


Both models are parsed to construct the following intermediate representation (imports omitted):

.. code-block:: rust
    
    let env = SMVEnv::new(&ctx);

    env.register_variable("counter", VarType::Int {
        init: Some(vec![0]),
        lower: Some(0),
        upper: Some(15),
    });

    env.reigster_variable("LED", VarType::Bool {
        init: Some(vec![true]),
    });

    env.register_predicate("reset",
        |_env, _ctx, _state| int_var!(_state, "counter")._eq(&Int::from_i64(_ctx, 15))
    );
    env.register_predicate("led_blink",
        |_env, _ctx, _state| (int_var!(_state, "counter") % &Int::from_i64(_ctx, 3))._eq(&Int::from_i64(_ctx, 2)) | predicate!("reset", _env, _ctx, _state)
    );

    // Defining Transitions
    env.register_transition("counter",
    |_env, _ctx, _state| exact!(Node, predicate!("reset", _env, _ctx, _state)),
    |_env, _ctx, _state| exact!(Int, 0)
    );
    env.register_transition("counter",
    |_env, _ctx, _state| exact!(Bool, true),
    |_env, _ctx, _state| exact!(Node, int_var!(_state, "counter") + &Int::from_i64(_ctx, 1))
    );

    env.register_transition("LED",
    |_env, _ctx, _state| exact!(Node, predicate!("led_blink", _env, _ctx, _state)),
    |_env, _ctx, _state| exact!(Bool, true)
    );
    env.register_transition("LED",
    |_env, _ctx, _state| exact!(Bool, true),
    |_env, _ctx, _state| exact!(Bool, false)
    );


References
----------

.. [1] NuSMV paper: https://nusmv.fbk.eu/papers/sttt_j/pdf/sttt_j.pdf
