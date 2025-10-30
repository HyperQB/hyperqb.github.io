Linearizability of Construction-Then-Read: Eliminating Partial Initialization (NuSMV)
===================================

Description of the Case Study
-----------------------------

This case study models an object that is constructed by one thread and observed by another. A constructor thread emits a construction-begun event and then writes two object fields in program order. A listener thread, after observing the event, reads both fields and produces return values derived from those reads. A “bad read” denotes any execution in which the listener has observed the construction event yet still reads a default (uninitialized) value from at least one field, reflecting a partially initialized state. The concurrent realization permits arbitrary interleavings between the constructor and listener, making such partial observations possible. The sequential reference realization delays the listener until construction has completed, ensuring that both reads observe initialized values and preventing bad reads. The linearizability requirement is that every behavior of the concurrent realization correspond to some behavior of the sequential reference with identical listener outcomes, which rules out executions exhibiting bad reads.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Concurrent

        .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/constructor/constructor_conc.smv
            :language: smv

    .. tab:: Sequential

        .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/constructor/constructor_seq.smv
            :language: smv

The HyperLTL formula
--------------------

Linearizability here requires that every concurrent execution of the construction-then-read scenario be observationally equivalent to a sequential execution in which the constructor's writes take effect at a single atomic point between its invocation and completion, prior to the listener's reads. When this property holds, it shows that the listener can never return values reflecting a partially initialized object, thereby ruling out bad reads and providing evidence that construction and memory-visibility semantics are correct under all thread interleavings.

.. math::

   \varphi_{\text{lin}} = \forall \pi_A.\exists \pi_B.\ \Box\left( \mathit{history}_{\pi_A} \leftrightarrow \mathit{history}_{\pi_B} \right)

.. tabs::

    .. tab:: Case Constructor

        .. literalinclude :: ../benchmarks_ui/nusmv/concurrency/constructor/linearizability.hq
            :language: hq

References
----------
