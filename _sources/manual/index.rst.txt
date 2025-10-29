HyperQB Manual
===================
HyperQB is a push-button, bounded model checker for verifying hyperproperties. Hyperproperties are systems-wide properties that express the behavior of system as a whole rather than the behavior of individual execution traces.

Installation
---------------

MacOS Binary installation
^^^^^^^^^^^^^^^^^^^^^^

Source code installation
^^^^^^^^^^^^^^^^^^^^^^


Modeling Languages
--------------------

HyperQB currently accepts input models in two languages:

   - **NuSMV** is a symbolic BBD-based model checker originated in CMU. The full documentation of the input language is available `here <https://nusmv.fbk.eu/user-manual.html>`_.

   - **Verilog** is a hardware description language. The IEEE standard documentation of Verilog 2005 is available `here <https://standards.ieee.org/ieee/1364/3641/>`_.

Specification Languages
------------------------

HyperLTL grammar
^^^^^^^^^^^^^^^^

A-HLTL grammar
^^^^^^^^^^^^^^^

Running HyperQB
---------------

GUI-based (standalone and web-based)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Command-line usage
^^^^^^^^^^^^^^^

This section provides a comprehensive overview of the command-line interface for HyperQB, detailing the various options and modes available for users to effectively utilize the tool. For details on input model languages and specification languages, please refer to the respective sections in this manual.

Synopsis
~~~~~~~~~

.. code-block:: text

   hyperqb -f <FORMULA> -n <FILE>... -k <K> -s <SEM> [-m <B>] [-c] [-q]
   hyperqb -f <FORMULA> -n <FILE>... -l
   hyperqb -f <FORMULA> -v <FILE>... -t <TOP_MODULE> -o <SMT2_FILE> -k <K> -s <SEM> [-m <B>] [-c] [-q]

Modes
~~~~~~~

Exactly **one** mode must be selected:

- ``-l, --loop_conditions``: Use loop conditions instead of unrolling.
- ``-k, --unrolling_bound <K>`` **with** ``-s, --semantics <SEM>``: Use bounded unrolling.

Inputs
~~~~~~~

Exactly **one** input model lanuage must be selected:

- ``-v, --verilog <FILE>...``: Yosys build file(s). Requires ``-t`` and ``-o``.
- ``-n, --nusmv <FILE>...``: NuSMV file(s).

- ``-f, --formula <FILE>``  
**Required.** Hyperproperty formula file. (Path)

Option Details
~~~~~~~~

.. grid:: 2 2 2 1
   :gutter: 2

   .. grid-item-card:: ``-f, --formula <FILE>``
      :class-card: sd-shadow-sm

      **Required.** Hyperproperty formula file. *(Path)*

   .. grid-item-card:: ``-v, --verilog <FILE>...``
      :class-card: sd-shadow-sm

      Yosys script(s). One or more paths, the number of paths provided should match the number of quantifiers in the provided formula file. **Requires** ``--top`` and ``--yosys_output``. *(Path)*

   .. grid-item-card:: ``-n, --nusmv <FILE>...``
      :class-card: sd-shadow-sm

      NuSMV file(s). One or more paths, the number of paths provided should match the number of quantifiers in the provided formula file. *(Path)*

   .. grid-item-card:: ``-t, --top <TOP_MODULE>``
      :class-card: sd-shadow-sm

      Top module name, this should match the module specified in the yosys script files. *(String)*

   .. grid-item-card:: ``-o, --yosys_output <SMT2_FILE>``
      :class-card: sd-shadow-sm

      Location of SMT2 file if using a build file, this should match the path specified in the yosys scripts. *(Path)*

   .. grid-item-card:: ``-l, --loop_conditions``
      :class-card: sd-shadow-sm

      Use loop conditions instead of unrolling. *(Flag)*

   .. grid-item-card:: ``-k, --unrolling_bound <K>``
      :class-card: sd-shadow-sm

      Unrolling bound. *(Unsigned integer)*

   .. grid-item-card:: ``-s, --semantics <SEM>``
      :class-card: sd-shadow-sm

      Choice of semantics: one of ``pes``, ``opt``, ``hpes``, ``hopt``. *(String)*

   .. grid-item-card:: ``-m, --trajectory_bound <B>``
      :class-card: sd-shadow-sm

      Trajectory bound. *(Unsigned integer)*

   .. grid-item-card:: ``-c, --counterexample``
      :class-card: sd-shadow-sm

      Generate counterexample if available. *(Flag)*

   .. grid-item-card:: ``-q, --qbf_solver``
      :class-card: sd-shadow-sm

      Use QBF solver (default is Z3). *(Flag)*

Examples
~~~~~~~

**Verilog + loop-conditions mode**

.. code-block:: bash

   hyperqb -f formula.hq -v build.ys build.ys -t main -o model.smt2 -k 15 -s pes -c

**Verilog with model with 2 models and counterexample generation**

.. code-block:: bash

   hyperqb -n benchmarks/loop_conditions/mm/mm1.smv benchmarks/loop_conditions/mm/mm2.smv -f benchmarks/loop_conditions/mm/mm.hq -l

**NuSMV + loop-conditions mode**


.. toctree::
   :hidden:

   installation
   languages
   specs
   running
