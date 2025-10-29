HyperQB Manual
===================
HyperQB is a push-button, bounded model checker for verifying hyperproperties. Hyperproperties are systems-wide properties that express the behavior of system as a whole rather than the behavior of individual execution traces.

.. grid:: 2 2 2 1
   :gutter: 2

   .. grid-item-card:: Installation
      :class-card: sd-shadow-sm

      - **MacOS Binary installation:**
      - **Source code installation:**

   .. grid-item-card:: Modeling Languages
      :class-card: sd-shadow-sm

      - HyperQB currently accepts input models in two languages:

         -- **NuSMV** is a symbolic BBD-based model checker originated in CMU. The full documentation of the input language is available `here <https://nusmv.fbk.eu/user-manual.html>`_.

         -- **Verilog** is a hardware description language. The IEEE standard documentation of Verilog 2005 is available `here <https://standards.ieee.org/ieee/1364/3641/>`_.

   .. grid-item-card:: Specification Languages
      :class-card: sd-shadow-sm

      - **HyperLTL grammar:**
      - **A-HLTL grammar:**

   .. grid-item-card:: Running HyperQB
      :class-card: sd-shadow-sm

      - **GUI-based (standalone and we-based):**

      Command-line usage
      ------------------

      This section provides a comprehensive overview of the command-line interface for HyperQB, detailing the various options and modes available for users to effectively utilize the tool. For details on input model languages and specification languages, please refer to the respective sections in this manual.

      Synopsis
      ^^^^^^^^

      .. code-block:: text

         hyperqb -f <FORMULA> -n <FILE>... -k <K> -s <SEM> [-m <B>] [-c] [-q]
         hyperqb -f <FORMULA> -n <FILE>... -l
         hyperqb -f <FORMULA> -v <FILE>... -t <TOP_MODULE> -o <SMT2_FILE> -k <K> -s <SEM> [-m <B>] [-c] [-q]

      Modes
      ^^^^^

      Exactly **one** mode must be selected:

      - ``-l, --loop_conditions``: Use loop conditions instead of unrolling.
      - ``-k, --unrolling_bound <K>`` **with** ``-s, --semantics <SEM>``: Use bounded unrolling.

      Inputs
      ^^^^^^

      Exactly **one** input model lanuage must be selected:

      - ``-v, --verilog <FILE>...``: Yosys build file(s). Requires ``-t`` and ``-o``.
      - ``-n, --nusmv <FILE>...``: NuSMV file(s).

      - ``-f, --formula <FILE>``  
      **Required.** Hyperproperty formula file. (Path)

      Option Details
      ^^^^^^^^^^^^^^

      - ``-v, --verilog <FILE>...``  
      Yosys build file(s). One or more paths. **Requires** ``--top`` and ``--yosys_output``. (Path)

      - ``-n, --nusmv <FILE>...``  
      NuSMV file(s). One or more paths. (Path)

      - ``-t, --top <TOP_MODULE>``  
      Top module name. Default: ``main``. (String)

      - ``-o, --yosys_output <SMT2_FILE>``  
      Location of SMT2 file if using a build file. (Path)

      - ``-l, --loop_conditions``  
      Use loop conditions instead of unrolling.

      - ``-k, --unrolling_bound <K>``  
      Unrolling bound. (Unsigned integer)

      - ``-s, --semantics <SEM>``  
      Choice of semantics: one of ``pes``, ``opt``, ``hpes``, ``hopt``. (String)

      - ``-m, --trajectory_bound <B>``  
      Trajectory bound. (Unsigned integer)

      - ``-c, --counterexample``  
      Generate counterexample if the formula is unsat.

      - ``-q, --qbf_solver``  
      Use QBF solver (default is Z3).

      Examples
      --------

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
