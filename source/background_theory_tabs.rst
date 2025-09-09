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

      .. rubric:: Asynchronous HyperLTL (A-HLTL: syntax and asynchronous semantics)

      **A-HLTL** augments HyperLTL with *trajectory quantifiers* that govern how traces progress relative to each other [2, 3]. In the BMC-oriented fragment (without next :math:`\bigcirc`):

      .. math::

         \begin{array}{rcl}
         \varphi &::=& \exists \pi.\,\varphi \mid \forall \pi.\,\varphi \mid E_\tau.\,\varphi \mid A_\tau.\,\varphi \mid \psi,\\
         \psi &::=& \mathit{true} \mid a_{\pi,\tau} \mid \neg \psi \mid \psi \lor \psi \mid \psi \land \psi \mid \psi \,\mathcal{U}\, \psi \mid \psi \,\mathcal{R}\, \psi.
         \end{array}

      A **trajectory** :math:`t` for the set of trace variables :math:`\mathrm{Paths}(\varphi)` is an :math:`\omega`-sequence :math:`t(0),t(1),\ldots` with :math:`t(i)\subseteq \mathrm{Paths}(\varphi)` indicating which traces advance at global step :math:`i` (others *stutter*). A trajectory is **fair** if every trace is selected infinitely often.

      We use a trajectory assignment :math:`\Gamma:\mathrm{Trajs}(\varphi)\rightharpoonup \mathrm{TRJ}` and an **asynchronous trace assignment** :math:`\Pi:\mathrm{Paths}(\varphi)\times \mathrm{Trajs}(\varphi)\to (2^{AP})^\omega\times \mathbb{N}` mapping :math:`(\pi,\tau)` to a pointed trace :math:`(\sigma,n)`. Define the successor :math:`(\Pi,\Gamma){+}1=(\Pi',\Gamma')` by incrementing :math:`n` exactly for those pairs with :math:`\pi\in \Gamma(\tau)(0)` and rotating the trajectories; write :math:`(\Pi,\Gamma){+}k` for the :math:`k`-fold iterate. Characteristic clauses (Boolean/quantifier cases as expected) are:

      .. math::

         \begin{aligned}
         &(\Pi,\Gamma)\vDash a_{\pi,\tau} &&\Leftrightarrow&& a\in \sigma(n)\ \text{ for }(\sigma,n)=\Pi(\pi,\tau),\\
         &(\Pi,\Gamma)\vDash \psi_1\,\mathcal{U}\,\psi_2 &&\Leftrightarrow&& \exists i\ge 0:\ (\Pi,\Gamma){+}i \vDash \psi_2\ \land\ \forall j<i:\ (\Pi,\Gamma){+}j \vDash \psi_1,\\
         &(\Pi,\Gamma)\vDash \psi_1\,\mathcal{R}\,\psi_2 &&\Leftrightarrow&& \forall i\ge 0:\ (\Pi,\Gamma){+}i \vDash \psi_2\ \text{or}\ \exists i\ge 0:\ (\Pi,\Gamma){+}i \vDash \psi_1 \land \forall j\le i:\ (\Pi,\Gamma){+}j \vDash \psi_2.
         \end{aligned}

      **Stutter-invariant fragment.** For bounded checking we restrict to formulas without :math:`\bigcirc`, so that inserted stuttering does not affect satisfaction; trajectories are assumed fair [2].


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

      .. rubric:: 4) QBF compilation

      For :math:`\varphi=Q_A\,\pi_A.\cdots Q_Z\,\pi_Z.\,\psi` (stutter-invariant), associate each :math:`\pi_j` with :math:`K_j` and build

      .. math::

         \text{⟦}\mathcal{K},\varphi\text{⟧}^{*}_k \;=\; Q_A\,\overline{x_A}\cdot Q_B\,\overline{x_B}\cdots Q_Z\,\overline{x_Z}\;
         \Big(\text{⟦}K_A\text{⟧}_k\ \circ_A\ \cdots\ \circ_Z\ \text{⟦}\psi\text{⟧}^{*}_{0,k}\Big),
         \qquad
         \circ_j=\begin{cases}\wedge & Q_j=\exists,\\ \rightarrow & Q_j=\forall.\end{cases}

      The QBF’s satisfiability is equivalent to the bounded satisfaction of :math:`\varphi` (and is exact on terminating systems under halting variants) [1, 2].


   .. tab-item:: Loop Condition Algorithm

      .. rubric:: Motivation

      Lasso constraints (prefix+loop) finitely represent infinite runs for LTL. For hyperproperties, different traces may loop at unrelated instants; a single synchronized loop is unsound/incomplete. **Efficient loop conditions** specialized to (A-)HyperLTL address this [3].

      .. rubric:: Automata-based completeness (one alternation)

      For fragments with at most one quantifier alternation (AE or EA), lasso-shaped witnesses suffice. Using Büchi-automata translations and product constructions yields a **completeness threshold** (worst-case doubly-exponential) such that increasing :math:`k` past the threshold cannot change SAT/UNSAT [3].

      .. rubric:: Simulation-based encodings (SIMEA/SIMAE)

      We avoid full automata by encoding **simulation** between explored prefixes.

      • **SIMEA (EA)**: search a lasso in the existential model and universally require the other model to simulate it.  
      • **SIMAE (AE)**: universally quantify a lasso in the first model and existentially find a simulating run in the second. When nondeterminism blocks simulation, introduce **prophecy variables** to pre-commit to choices enabling alignment.

      A (forward) simulation :math:`R\subseteq S_P\times S_Q` between Kripke structures :math:`K_P,K_Q` satisfies

      .. math::

         \begin{aligned}
         &\forall s_P^0\in S_P^0\,\exists s_Q^0\in S_Q^0:\ (s_P^0,s_Q^0)\in R,\qquad &&L_P(s_P)=L_Q(s_Q)\ \text{for }(s_P,s_Q)\in R,\\
         &\forall (s_P,s_Q)\in R,\ \forall (s_P,s_P')\in \delta_P\ \exists (s_Q,s_Q')\in \delta_Q:\ (s_P',s_Q')\in R.
         \end{aligned}

      .. rubric:: Encoding skeleton (AE example :math:`\forall \pi.\exists \pi'.\,\Box\,\mathsf{Pred}`)

      1) Select a lasso in :math:`K_P` via loop-selector Booleans.

      2) Declare Booleans for a run of :math:`K_Q` and a matrix :math:`\mathsf{sim}_{i,j}` for the candidate relation.

      3) Constrain initials and step-preservation so that :math:`\mathsf{sim}` is a simulation; enforce label agreement for :math:`\mathsf{Pred}`.

      4) (Optional) Add **prophecy** variables to resolve nondeterminism and enable alignment.

      The EA case dually selects the lasso in the existential model and universally quantifies the simulation obligation.

      .. rubric:: Scope and benefits

      • Captures early loops/infinite behavior with finite exploration.  
      • Often explores only a subset of a large model yet remains conclusive.  
      • Produces compact witnesses/counterexamples.  
      • Targeted at **one** alternation (AE/EA); for A-HLTL BMC we remain in the **stutter-invariant** fragment.