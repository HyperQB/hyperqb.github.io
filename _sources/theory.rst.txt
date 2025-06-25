Background Theory
=================

Given a HyperLTL formula :math:`\varphi`, a bound :math:`k`, and a set of Kripke structures :math:`\mathcal{K}`, the goal is to construct a :math:`\text{QBF}` formula :math:`⟦ \mathcal{K}, \varphi ⟧_k` whose satisfiability reflects whether :math:`\mathcal{K} \models \varphi` holds within bound :math:`k`.

Encoding the Kripke Structures
------------------------------

To reduce model checking to QBF, each Kripke structure is encoded as a Boolean formula representing all its valid traces up to a fixed bound :math:`k`.

- States are encoded using fresh Boolean variables :math:`n_0, n_1, \dots`, added to the set of atomic propositions:
  :math:`\mathit{AP}^* = \mathit{AP} \cup \{n_0, n_1, \dots\}`.

- The initial condition is a formula :math:`I_A` over :math:`\mathit{AP}^*`

- The transition relation is encoded as :math:`R_A(x, x')`, where :math:`x` and :math:`x'` represent states at consecutive time steps.

- For each position :math:`i = 0` to :math:`k`, a copy :math:`x_A^i` of the variables is introduced. For a structure :math:`K_A` and bound :math:`k`, the unrolled encoding is:

  .. math::

     ⟦K_A⟧_k = I_A(x_A^0) \land R_A(x_A^0, x_A^1) \land \dots \land R_A(x^{k-1}_A,x^k_A)

This formula represents all traces of length :math:`k` from the Kripke structure, and provides the basis for checking temporal properties using QBF.

Encoding the Inner LTL Formula
------------------------------

The inner LTL formula is translated into a Boolean formula over the unrolled trace, using standard bounded model checking (BMC) techniques with semantic variations.

- The formula is encoded inductively as :math:`⟦ \psi ⟧_i^k`, where :math:`i` is the current time step and :math:`k` is the bound.
- There are four variants depending on semantics: pessimistic, optimistic, halting pessimistic, and halting optimistic.

**Inductive rules (common to all semantics)**:

.. math::

   \begin{align}
   &⟦p_\pi⟧^{*}_{i,k} &:=\ &p_\pi^i \\
   &⟦\neg p_\pi⟧^{*}_{i,k} &:=\ &\neg p_\pi^i \\
   &⟦\psi_1 \lor \psi_2⟧^{*}_{i,k} &:=\ &⟦\psi_1⟧^{*}_{i,k} \lor ⟦\psi_2⟧^{*}_{i,k} \\
   &⟦\psi_1 \land \psi_2⟧^{*}_{i,k} &:=\ &⟦\psi_1⟧^{*}_{i,k} \land ⟦\psi_2⟧^{*}_{i,k} \\
   &⟦\psi_1 \mathcal{U} \psi_2⟧^{*}_{i,k} &:=\ &⟦\psi_2⟧^{*}_{i,k} \lor (⟦\psi_1⟧^{*}_{i,k} \land ⟦\psi_1 \mathcal{U} \psi_2⟧^{*}_{i+1,k}) \\
   &⟦\psi_1 \mathcal{R} \psi_2⟧^{*}_{i,k} &:=\ &⟦\psi_2⟧^{*}_{i,k} \land (⟦\psi_1⟧^{*}_{i,k} \lor ⟦\psi_1 \mathcal{R} \psi_2⟧^{*}_{i+1,k}) \\
   &⟦\bigcirc \psi⟧^{*}_{i,k} &:=\ &⟦\psi⟧^{*}_{i+1,k}
   \end{align}

**Base cases** depend on the semantic variant and define the value beyond bound :math:`k`:

.. math::

   \begin{align}
   &⟦\psi⟧^{\text{pes}}_{k+1,k} := \text{false} &&⟦\psi⟧^{\text{opt}}_{k+1,k} := \text{true} \\
   &⟦\psi⟧^{\text{hpes}}_{k+1,k} := ⟦\text{halted}⟧^{\text{hpes}}_{k,k} \land ⟦\psi⟧^{\text{hpes}}_{k,k}
   &&⟦\psi⟧^{\text{hopt}}_{k+1,k} := ⟦\text{halted}⟧^{\text{hopt}}_{k,k} \rightarrow ⟦\psi⟧^{\text{hopt}}_{k,k}
   \end{align}
These base cases affect how temporal operators are evaluated at the final unrolling step.

Combining the Encodings
-----------------------

Let :math:`\varphi = \mathbb{Q}_A \pi_A. \mathbb{Q}_B \pi_B. \dots \mathbb{Q}_Z \pi_Z. \psi` be a HyperLTL formula, and let each :math:`\pi_j` be associated with a Kripke structure :math:`K_j`.

The full QBF encoding is:

.. math::

   ⟦\mathcal{K}, \varphi⟧^{*}_k =
   \mathbb{Q}_A \overline{x_A} \cdot \mathbb{Q}_B \overline{x_B} \cdots \mathbb{Q}_Z \overline{x_Z} \left(
   ⟦K_A⟧_k \circ_A ⟦K_B⟧_k \circ_B \cdots ⟦K_Z⟧_k \circ_Z ⟦\psi⟧^{*}_{0,k}
   \right)

Where:
    - :math:`⟦ K_j ⟧_k` is the unrolling of Kripke structure :math:`K_j`
    - :math:`\circ_j = \wedge` if :math:`\mathbb{Q}_j = \exists`, and :math:`\rightarrow` if :math:`\mathbb{Q}_j = \forall` for :math:`\in \mathit{Vars}(\varphi)`
    - :math:`⟦ \psi ⟧_0^k` is the encoding of the LTL subformula under the chosen semantics

This combined formula allows a QBF solver to decide whether the HyperLTL formula holds for all (or some) traces up to bound :math:`k`.

References
----------

A more detailed explanation can be found in the paper `Bounded Model Checking for Hyperproperties <https://www.cse.msu.edu/tart/sites/default/files/publications/files/2021-07/tacas21.pdf>`_ *Tzu-Han Hsu, César Sánchez, and Borzoo Bonakdarpour*
