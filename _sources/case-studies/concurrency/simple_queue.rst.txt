Linearizability: Simple Queue (NuSMV)
======================================

Description of the Case Study
-----------------------------

This benchmark captures a bounded first-in first-out queue built as a circular buffer with five slots :ref:`[HS08] <HS08>`. Two
threads interleave enqueue and dequeue operations by reading and updating shared `head` and `tail` indices as well as the array
cells that hold queued values. The queue is designed so that successful operations mimic a linearizable FIFO behavior, but
concurrent schedules may reorder the value that is ultimately dequeued.

The concurrent NuSMV model steps both threads through their enqueue/dequeue phases and records the value removed from the queue
on each execution. The sequential specification executes the same operations atomically, producing a canonical removal value.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Case #1

        .. tabs::

            .. tab:: Simple queue concurrent

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/simple_queue/concurrent.smv
                    :language: smv

            .. tab:: Simple queue sequential

                .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/simple_queue/atomic.smv
                    :language: smv

The HyperLTL formula(s)
-----------------------

The observational-determinism requirement demands that all executions remove identical values at every step, regardless of the
interleaving. HyperQB discovers a counterexample where two traces disagree on the dequeued value, demonstrating the queue’s
non-linearizable behaviour.

.. math::

   \varphi_{\text{det}} = \forall \pi_A.\forall \pi_B.\ \Box \left( \mathit{removed}_{\pi_A} = \mathit{removed}_{\pi_B} \right)

.. tabs::

    .. tab:: Case #1

        .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/simple_queue/lin.hq
            :language: hq

References
----------

.. _HS08:

- [HS08] `M. Herlihy and N. Shavit. *The Art of Multiprocessor Programming*. Morgan Kaufmann, 2008.`

.. _HW90:

- [HW90] `M. Herlihy and J. M. Wing. Linearizability: A correctness condition for concurrent objects. ACM Transactions on Programming Languages and Systems, 12(3):463–492, 1990. <https://doi.org/10.1145/78969.78972>`_
