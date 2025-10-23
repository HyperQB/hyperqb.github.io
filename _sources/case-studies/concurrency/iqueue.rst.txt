Linearizability: IQueue (NuSMV)
================================

Description of the Case Study
-----------------------------

This benchmark models a bounded lock-free queue similar to the ring-buffer design presented in :ref:`[HS08] <HS08>`. Two worker
threads repeatedly enqueue and dequeue values from a circular array with three slots. Each operation performs a sequence of
compare-and-set loops on the shared head and tail indices before committing an update, and both operations can fail—enqueue
when the queue is full and dequeue when it is empty. *Linearizability* :ref:`[HW90] <HW90-IQueue>` requires that every concurrent
history of these operations match some sequential execution with the same invocations, responses, and failure outcomes.

The concurrent NuSMV specification follows the enqueue/dequeue state machines of both processes, recording when each operation
is in progress, when it terminates, and whether it failed because of contention or an empty queue. The sequential specification
executes the same operations atomically on an abstract circular buffer while preserving the same failure semantics. With
pessimistic semantics, a bounded counterexample suffices to disprove linearizability. *HyperQB* explores the benchmark under
this semantics, producing either a witness that exposes a mismatch between the two traces or a proof that no such witness
exists within the chosen bound.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Case #1

        .. tabs::

            .. tab:: IQueue concurrent

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/iqueue/iqueue_conc.smv
                    :language: smv

            .. tab:: IQueue sequential

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/iqueue/iqueue_seq.smv
                    :language: smv

The HyperLTL formula(s)
-----------------------

The linearizability formula insists that every observable history of enqueue and dequeue events has a matching sequential
execution. The existential trace captures the serial specification; any mismatch in operation order or return values exposes a
bug.

.. math::

   \varphi_{\text{lin}} = \forall \pi_A.\exists \pi_B.\ \Box\left( \mathit{history}_{\pi_A} \leftrightarrow \mathit{history}_{\pi_B} \right)

.. tabs::

    .. tab:: Case #1

        .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/iqueue/iqueue.hq
            :language: hq

References
----------

.. _HS08:

- [HS08] `M. Herlihy and N. Shavit. *The Art of Multiprocessor Programming*. Morgan Kaufmann, 2008.`


.. _HW90-IQueue:

- [HW90] `M. Herlihy and J. M. Wing. Linearizability: A correctness condition for concurrent objects. ACM Transactions on Programming Languages and Systems, 12(3):463–492, 1990. <https://doi.org/10.1145/78969.78972>`_
