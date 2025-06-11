.. HyperQB documentation master file, created by
   sphinx-quickstart on Thu Jun  5 17:06:11 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to HyperQB!
===================

**HyperQB** is a home-grown tool for *Bounded Model Checking* of Hyperproperties using a QBF-based algorithm.

HyperQB includes several parts:

- NuSMV model parsing and Boolean encoding of the transition relation
- HyperLTL formula translation
- QBF encoding of unfolding with bound ``k`` using bounded semantics
- QBF solving with a QBF solver (currently QuAbs)

License
-------

Our code is under the MIT license (see ``LICENSE.tex``), while the included tool QuAbs is under the AGPL license.

Get Started
-----------

You can start using HyperQB in two simple steps:

1. First install `Docker <https://docs.docker.com/get-docker/>`_. HyperQB will automatically pull the image and execute scripts to avoid dependency issues.
2. Clone the repository and enter the folder:

   .. code-block:: bash

      git clone https://github.com/TART-MSU/HyperQB.git
      cd HyperQB

You are now ready to run HyperQB! :D

First Demo
----------

To verify everything works, run any of the following (from the ``HyperQB/`` directory):

.. code-block:: bash

   sudo ./hyperqb.sh demo/mini.smv demo/mini.smv demo/mini.hq 3 -pes -bughunt
   sudo ./hyperqb.sh demo/mini2.smv demo/mini2.smv demo/mini2.hq 3 -pes -find
   sudo ./hyperqb.sh demo/infoflow.smv demo/infoflow.smv demo/infoflow1.hq 5 -pes -debug

You can find more examples in the ``run_demo.sh`` script.

How to Use
----------

To run HyperQB:

.. code-block:: bash

   ./hyperqb.sh <list of models> <formula> <k> <sem> <mode>

**Arguments:**

- ``<list of models>``: SMV files (NuSMV format)
- ``<formula>``: .hq file in our custom grammar
- ``<k>``: natural number (unrolling bound)
- ``<sem>``: semantics (`-pes`, `-opt`, `-hpes`, or `-hopt`)
- ``<mode>``: mode of use (`-bughunt` for negated formula or `-find` for original formula)

**Examples:**

.. code-block:: bash

   ./hyperqb.sh demo/bakery.smv demo/bakery.smv demo/symmetry.hq 10 -pes -bughunt
   ./hyperqb.sh demo/snark_conc.smv demo/snark1_seq.smv demo/lin.hq 18 -pes -bughunt

Benchmarks
----------

All benchmark models and formulas are located in the ``benchmarks/`` directory.

You can run benchmarks using:

.. code-block:: bash

   ./run_benchmarks.sh <case#>   # Run specific case
   ./run_benchmarks.sh -all      # Run all cases

Examples:

.. code-block:: bash

   ./run_benchmarks.sh 0.3 # Runs case #0.3
   ./run_benchmarks.sh 9.2 # Runs case #9.2

**Benchmark categories:**

- Case #1.1-#1.4: Symmetry in the Bakery Algorithm
- Case #2.1-#2.2: Linearizability in SNARK Algorithm
- Case #3.1-#3.2: Non-interference in Typed Multi-threaded Programs
- Case #4.1-#4.2: Fairness in Non-repudiation Protocols
- Case #5.1-#5.2: Privacy-Preserving Path Synthesis for Robots
- Case #6.1: Mutant Synthesis for Mutation Testing
- Case #7.1: Co-termination of multiple programs
- Case #6.1: Mutant Synthesis for Mutation Testing
- Case #6.1: Mutant Synthesis for Mutation Testing
- Case #6.1: Mutant Synthesis for Mutation Testing
- Case #6.1: Mutant Synthesis for Mutation Testing
- Case #7.1: Co-termination
- Case #8.1: Deniability
- Case #9.1 - #9.3: Intransitive Non-interference
- Case #10.1 - #10.2: TINI and TSNI
- Case #11.1: K-safety
- Case #12.1: MapSynth
- Case #12.2: MapSynth
- Case #13.1: TeamLTL
- Case #13.2: TeamLTL
- Case #14.1: Non-deterministic init
- Case #14.2: Non-deterministic trans

Live Demo
----------------------
.. raw:: html

   <iframe src="https://hyperqb.egr.msu.edu/" width="100%" height="950px" style="border:1px solid #ccc;">
   </iframe>

Additional Information
----------------------

**NuSMV Models**

HyperQB supports most NuSMV feature/keywords (``VAR``, ``ASSIGN``, ``DEFINE``, etc.).  
It does **not** support the keyword ``process`` (for asynchronicity). but this can be modeled with nondeterminism:

.. code-block:: smv

   next(proc_PC) := {0,1};  -- nondeterministic behavior

**HyperLTL Formulas**

We do not use the ``SPEC`` keyword from NuSMV. Instead, write formulas in a `.hq` file using our own grammar.

People
------

- `Tzu-Han Hsu <https://tzuhancs.github.io/>`_, Michigan State University
- `Borzoo Bonakdarpour <http://www.cse.msu.edu/~borzoo/>`_, Michigan State University
- `César Sánchez <https://software.imdea.org/~cesar/>`_, IMDEA Software Institute

Publication
-----------

- `Bounded Model Checking for Hyperproperties (TACAS'21) <https://link.springer.com/content/pdf/10.1007/978-3-030-72016-2_6.pdf>`_