Linearizability: Lazy List Set (NuSMV)
=====================================

Description of the Case Study
-----------------------------

This case study encodes the lazy list set algorithm of Heller, Herlihy, Shavit, and Tzafrir :ref:`[HHST05] <HHST05>` in NuSMV.
Two threads traverse a sorted linked list while holding fine-grained locks to insert, remove, or lookup a single shared key.
Logical deletion followed by physical removal makes it possible for one thread to observe stale membership information when a
second thread interleaves between validation and commit. *Linearizability* :ref:`[HW90] <HW90-Lazy>` demands that every concurrent
history of these operations corresponds to some sequential history that contains the same invocations and responses.

The concurrent model captures the standard lazy-list phases—traverse, lock predecessor and current nodes, validate links, and
then perform the update—along with boolean return values for add, remove, and contains. The sequential specification executes
the same operations atomically over the abstract set. Using pessimistic semantics, a bounded counterexample suffices to refute
linearizability. *HyperQB* reports SAT for this benchmark, producing a witness where a lookup returns stale information because
validation passed just before another thread removed the target node, reproducing the classic lazy-list violation.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Case #1

        .. tabs::

            .. tab:: Lazy list concurrent

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/lazy_list/lazy_list_conc.smv
                    :language: smv

            .. tab:: Lazy list sequential

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/lazy_list/lazy_list_seq.smv
                    :language: smv

The HyperLTL formula(s)
-----------------------

Linearizability is expressed by equating the invocation and response history of the concurrent lazy-list execution with that of
a sequential witness. If the concurrent run ever observes a lookup result that cannot be produced sequentially, the formula is
violated.

.. math::

   \varphi_{\text{lin}} = \forall \pi_A.\exists \pi_B.\ \Box\left( \mathit{history}_{\pi_A} \leftrightarrow \mathit{history}_{\pi_B} \right)

.. tabs::

    .. tab:: Case #1

        .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/lazy_list/lazy_list.hq
            :language: hq

References
----------

.. _HHST05:

- [HHST05] `D. Heller, M. Herlihy, N. Shavit, and M. Tzafrir. A lazy concurrent list-based set algorithm. In *Proceedings of the 9th International Symposium on Distributed Computing (DISC)*, pages 3–16, 2005. <https://doi.org/10.1007/11561927_3>`_

.. _HW90-Lazy:

- [HW90] `M. Herlihy and J. M. Wing. Linearizability: A correctness condition for concurrent objects. ACM Transactions on Programming Languages and Systems, 12(3):463–492, 1990. <https://doi.org/10.1145/78969.78972>`_
