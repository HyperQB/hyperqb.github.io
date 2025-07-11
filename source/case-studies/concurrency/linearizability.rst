Linearizability
===============

Description of the Case Study
-----------------------------

The second study consists on verifying linearizability of the SNARK concurrent datatype :ref:`[DDG+04] <DDG+04>`. SNARK implements a
concurrent double-ended queue using double-compare-and-swap (DCAS) and a doubly linked-list. *Linearizability* :ref:`[HW90] <HW90>` is a
hyperproperty that requires that any *history* of execution of a concurrent data structure—where history is sequence of
*invocations* and *responses* by different threads—matches some sequential order of invocations and responses.

.. math::

   \varphi_{\text{lin}} = \forall \pi_A.\exists \pi_B.\ \Box\left( \mathit{history}_{\pi_A} \leftrightarrow \mathit{history}_{\pi_B} \right)

SNARK is known to have two linearizability bugs. With the use of *pessimistic semantics*, a witness of linearizability
violation of length :math:`k` is enough to infer that the given system does not satisfy the linearizability property.
*HyperQB* returns SAT identifying both bugs and producing two counterexamples. The bugs returned are consistent with the
ones reported in :ref:`[DDG+04] <DDG+04>`.



Benchmarks
----------

.. tabs::

    .. tab:: Case #2.1

        **The Model(s)**

        .. tabs::

            .. tab:: Snark 1 M1 concurrent

                .. literalinclude :: ../models/2_snark/snark1_M1_concurrent.smv
                    :language: smv

            .. tab:: Snark 1 M2 sequential

                .. literalinclude :: ../models/2_snark/snark1_M2_sequential.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../models/2_snark/snark1.hq
            :language: smv

    .. tab:: Case #2.2

            **The Model(s)**

            .. tabs::

                .. tab:: Snark 2 M1 concurrent

                    .. literalinclude :: ../models/2_snark/snark2_M1_concurrent.smv
                        :language: smv

                .. tab:: Snark 2 M2 sequential

                    .. literalinclude :: ../models/2_snark/snark2_M2_sequential.smv
                        :language: smv

            **Formula**

            .. literalinclude :: ../models/2_snark/snark2.hq
                :language: smv

References
----------
.. _DDG+04:
- [DDG+04] S. Doherty, D. Detlefs, L. Groves, C. H. Flood, V. Luchangco, P. A. Martin, M. Moir, N. Shavit, and G. L. Steele Jr. DCAS is not a silver bullet for nonblocking algorithm design. In *Proceedings of the 16th Annual ACM Symposium on Parallelism in Algorithms and Architectures (SPAA)*, pages 216–224, 2004.
.. _HW90:
- [HW90] M. Herlihy and J. M. Wing. Linearizability: A correctness condition for concurrent objects. ACM Transactions on Programming Languages and Systems, 12(3):463–492, 1990.