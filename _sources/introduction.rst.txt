Introduction
============

**HyperQB** is a *push-button*, **QBF-based bounded model checker** for verifying **hyperproperties**.
It takes as input a NuSMV model and a formula expressed in the temporal logic HyperLTL. Our QBF-based technique allows
HyperQB to seamlessly deal with quantifier alternations. Based on the selection of either bug hunting or synthesis,
the instances of counterexamples (for negated formula) or witnesses (for synthesis of positive formulas) are returned.

Overview
--------

- **Inputs**:
    - A set of models (up to one per trace quantifier)
    - A **HyperLTL** formula specifying the hyperproperty

- **Outputs**:
    - Dissatisfaction and *Counterexample*
    - Satisfaction and *Witness*

- **Core Technique**:
    1. Parse the inputs into Boolean/unrolled representations.
    2. Encode model plus temporal formula up to bound *k* as a **QBF**.
    3. Solve the QBF with a solver (currently **QuAbs**), then decode result back into:
        - A **counterexample** (bug hunting), or
        - A **witness** (trace set satisfying the property)