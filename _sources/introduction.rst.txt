Introduction
============

**HyperQB** is a *push-button*, **bounded model checker** for verifying **hyperproperties**.
Hyperproperties [1] are systems-wide properties that express the behavior of system as a whole rather than the behavior of individual execution traces.
Hyperproperties can express important information-flow security policies (e.g., confidentiality and integrity), consistency models in concurrent computing (e.g., linearizability [2]]), robustness conditions in cyber-physical
systems [3], and path planning in multi-agent systems.

Overview
--------
It takes as input a NuSMV model and a formula expressed in the temporal logic HyperLTL. Our QBF-based technique allows
HyperQB to seamlessly deal with quantifier alternations. Based on the selection of either bug hunting or synthesis,
the instances of counterexamples (for negated formula) or witnesses (for synthesis of positive formulas) are returned.

.. figure:: _static/flowchart.png
   :scale: 80 %
   :alt: Internal architechture of HyperQB
   :align: center


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

[1] Michael R. Clarkson, Fred B. Schneider: **Hyperproperties.** Journal of Computer Security 18(6): 1157-1210 (2010)
