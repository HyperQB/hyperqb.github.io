Introduction
============

**HyperQB** is a *push-button*, **bounded model checker** for verifying **hyperproperties**.
Hyperproperties [1] are systems-wide properties that express the behavior of system as a whole rather than the behavior of individual execution traces.
Hyperproperties can express important information-flow security policies (e.g., confidentiality and integrity), consistency models in concurrent computing (e.g., linearizability [2]]), robustness conditions in cyber-physical
systems `[WZBP19] <https://www.cse.msu.edu/tart/publication/statistical-verification-hyperproperties-cyber-physical-systems>`_, and path planning in multi-agent systems.
The core technology of HyperQB as a bounded model checker is based on an efficient transformation of the verification problem to solving the satisfiability problem for qunatified boolean formulas (QBF) and modulo theory (SMT).

Overview
--------
HyperQB can build and analyze several types of input models and temporal-logic specifications for hyperproperties.
The QBF/SMT-based technique allows HyperQB to seamlessly deal with quantifier alternations.
Based on the selection of either bug hunting or synthesis, the instances of counterexamples (for negated formula) or witnesses (for synthesis of positive formulas) are returned.

.. figure:: _static/flowchart.png
   :scale: 80 %
   :alt: Internal architechture of HyperQB
   :align: center


- **Inputs**:
    - A set of models (up to one per trace quantifier) in **NuSMV** or **Verilog** languages (the C -> LLVM path is still under construction) 
    - A **HyperLTL** [3] or **A-HLTL** `[BCBFS21] <https://www.cse.msu.edu/tart/publication/temporal-logic-asynchronous-hyperproperties>`_ formula specifying the hyperproperty
    - The type of bounded semantics `[HSB21] <https://www.cse.msu.edu/tart/publication/bounded-model-checking-hyperproperties>`_
    - The type of loop condition `[HSSB23] <https://www.cse.msu.edu/tart/publication/efficient-loop-conditions-bounded-model-checking-hyperproperties>`_
    - SMT or QBF decision procedure

- **Outputs**:
    - Dissatisfaction and *Counterexample*
    - Satisfaction and *Witness*

- **Core Technique**:
    - After parse the inputs into Boolean/SMT unrolled representations, the model(s) and specification are unrolled up to a bound *k* as a **QBF** or **SMT** instance `[HSB21] <https://www.cse.msu.edu/tart/publication/bounded-model-checking-hyperproperties>`_ `[HBFS23] <https://www.cse.msu.edu/tart/publication/bounded-model-checking-asynchronous-hyperproperties>`_. Then, a solver QBF/SMT (currently **QuAbs/Z3**) will solve the decision problem and decode the result back into a **counterexample** (bug hunting), or a **witness** (trace set satisfying the property).

Sponsors
--------
.. figure:: _static/NSF-Symbol.png
   :scale: 100 %
   :alt: NSF
   :align: center


[1] M. R. Clarkson and F. B. Schneider: **Hyperproperties.** Journal of Computer Security 18(6): 1157-1210 (2010)

[2] M. Herlihy and J. M. Wing. Linearizability: A correctness condition for concurrent objects. ACM Transactions on Programming Languages and Systems, 12(3):463–492 (1990)

[3] M. R. Clarkson, B. Finkbeiner, M. Koleini, K. K. Micinski, M. N. Rabe, C. Sánchez: Temporal Logics for Hyperproperties. POST 2014: 265-284
