Introduction
============

**HyperQB** is a *push-button*, **bounded model checker** for verifying **hyperproperties**.
Hyperproperties [1] are systems-wide properties that express the behavior of system as a whole rather than the behavior of individual execution traces.
Hyperproperties can express important information-flow security policies (e.g., confidentiality and integrity), consistency models in concurrent computing (e.g., linearizability [2]]), robustness conditions in cyber-physical
systems [3], and path planning in multi-agent systems.
The core technology of HyperQB as a bounded model checker is an efficient transformation of the verification problem to solving the satisfiability problem for qunatified boolean formulas (QBF) and modulo theory (SMT).

Overview
--------
HyperQB can build and analyse many types It takes as input a NuSMV model and a formula expressed in the temporal logic HyperLTL. Our QBF-based technique allows
HyperQB to seamlessly deal with quantifier alternations. Based on the selection of either bug hunting or synthesis,
the instances of counterexamples (for negated formula) or witnesses (for synthesis of positive formulas) are returned.

.. figure:: _static/flowchart.png
   :scale: 70 %
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

Sponsors
--------
.. figure:: _static/NSF-Symbol.png
   :scale: 20 %
   :alt: NSF
   :align: center


[1] M. R. Clarkson and F. B. Schneider: **Hyperproperties.** Journal of Computer Security 18(6): 1157-1210 (2010)
[2] M. Herlihy and J. M. Wing. Linearizability: A correctness condition for concurrent objects. ACM Transactions on Programming Languages and Systems, 12(3):463–492 (1990)
[3] Y. Wang, M. Zarei, B. Bonakdarpour, Miroslav Pajic: Statistical Verification of Hyperproperties for Cyber-Physical Systems. ACM Transactions on Embedded Computing Systems 18(5s): 92:1-92:23 (2019)
