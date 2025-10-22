Linearizability: Explicit Memory Management ABA (NuSMV)
======================================================

Description of the Case Study
-----------------------------

This case study models the Treiber stack :ref:`[Tre86] <Tre86>` under explicit memory management (EMM). Two threads share a stack implemented over a pair of reusable nodes. Once a pop returns a node to the free list, it becomes immediately available for the next push, recreating the classical ABA scenario. *Linearizability* :ref:`[HW90] <HW90>` requires that every
concurrent history of push and pop operations can be matched by some sequential execution that preserves invocation and
response order.

The concurrent NuSMV model explicitly tracks when each thread invokes, completes, and succeeds at push or pop, while the
sequential specification executes the same operations one at a time. Under pessimistic semantics, a bounded counterexample is
sufficient to disprove linearizability. *HyperQB* flags the model as SAT within the given bound, producing a witness where a
thread observes a recycled node whose value no longer matches a valid sequential history, exposing the ABA bug that arises without reclamation safeguards.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Case #1

        .. tabs::

            .. tab:: EMM-ABA concurrent

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/emm_aba/emm_aba_conc.smv
                    :language: smv

            .. tab:: EMM-ABA sequential

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/emm_aba/emm_aba_seq.smv
                    :language: smv

The HyperLTL formula(s)
-----------------------

Linearizability compares the operation histories of a concurrent execution with those of a sequential witness. If every step of
the histories aligns, the concurrent execution is considered correct; any divergence reveals a violation.

.. math::

   \varphi_{\text{lin}} = \forall \pi_A.\exists \pi_B.\ \Box\left( \mathit{history}_{\pi_A} \leftrightarrow \mathit{history}_{\pi_B} \right)

.. tabs::

    .. tab:: Case #1

        .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/emm_aba/emm_aba.hq
            :language: hq

References
----------

.. _Tre86:

- [Tre86] `R. K. Treiber. Systems programming: Coping with parallelism. IBM Technical Report RJ 5118, 1986. <https://domino.research.ibm.com/library/cyberdig.nsf/papers/580134C90DB2A1C78525779800566C94>`_


.. _HW90:

- [HW90] `M. Herlihy and J. M. Wing. Linearizability: A correctness condition for concurrent objects. ACM Transactions on Programming Languages and Systems, 12(3):463–492, 1990. <https://doi.org/10.1145/78969.78972>`_
