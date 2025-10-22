Linearizability: SNARK (NuSMV)
=======================

Description of the Case Study
-----------------------------

The second case study verifies linearizability of the SNARK concurrent datatype :ref:`[DDG+04] <DDG+04>`. SNARK implements a
concurrent double-ended queue using double-compare-and-swap (DCAS) and a doubly linked-list. *Linearizability* :ref:`[HW90] <HW90>` is a
hyperproperty that requires that any *history* of execution of a concurrent data structure—where history is sequence of
*invocations* and *responses* by different threads—matches some sequential order of invocations and responses.

SNARK is known to have two linearizability bugs. With the use of *pessimistic semantics*, a witness of linearizability
violation of length :math:`k` is enough to infer that the given system does not satisfy the linearizability property.
*HyperQB* returns SAT identifying both bugs and producing two counterexamples. The bugs returned are consistent with the
ones reported in :ref:`[DDG+04] <DDG+04>`.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Case #2.1

        .. tabs::

            .. tab:: Snark 1 M1 concurrent

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/snark/snark1_conc.smv
                    :language: smv

            .. tab:: Snark 1 M2 sequential

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/snark/snark1_seq.smv
                    :language: smv

    .. tab:: Case #2.2

        .. tabs::

            .. tab:: Snark 2 M1 concurrent

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/snark/snark2_M1_concurrent.smv
                    :language: smv

            .. tab:: Snark 2 M2 sequential

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/snark/snark2_M2_sequential.smv
                    :language: smv

The HyperLTL formula(s)
-----------------------

Linearizability forces the concurrent SNARK histories to match those of a sequential witness. Both benchmark variants use the
same HyperLTL template; HyperQB produces counterexamples demonstrating the two known bugs.

.. math::

   \varphi_{\text{lin}} = \forall \pi_A.\exists \pi_B.\ \Box\left( \mathit{history}_{\pi_A} \leftrightarrow \mathit{history}_{\pi_B} \right)

.. tabs::

    .. tab:: Case #2.1

        .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/snark/lin.hq
            :language: hq

    .. tab:: Case #2.2

        .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/snark/snark2.hq
            :language: hq

References
----------

.. _DDG+04:

- [DDG+04] `S. Doherty, D. Detlefs, L. Groves, C. H. Flood, V. Luchangco, P. A. Martin, M. Moir, N. Shavit, and G. L. Steele Jr. DCAS is not a silver bullet for nonblocking algorithm design. In *Proceedings of the 16th Annual ACM Symposium on Parallelism in Algorithms and Architectures (SPAA)*, pages 216–224, 2004. <https://doi.org/10.1145/1007912.1007945>`_

.. _HW90:

- [HW90] `M. Herlihy and J. M. Wing. Linearizability: A correctness condition for concurrent objects. ACM Transactions on Programming Languages and Systems, 12(3):463–492, 1990. <https://doi.org/10.1145/78969.78972>`_
