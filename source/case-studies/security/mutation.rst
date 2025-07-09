Mutation testing
================

Description of the Case Study
-----------------------------

Another application of hyperproperties with quantifier
alternation is the efficient generation of test suites for mutation testing. We
borrow a model from :ref:`[FBW19] <FBW19>` and apply the original formula that describes a good
test mutant together with the model, expressed as:

.. math::

   \varphi_{\text{mut}} = \exists \pi_A . \forall \pi_B \left(
   mut_{\pi_A} \land \neg mut_{\pi_B} \right) \land
   \left(
     \left( in_{\pi_A} \leftrightarrow in_{\pi_B} \right) \
     \mathcal{U} \
     \left( out_{\pi_A} \not\leftrightarrow out_{\pi_B} \right)
   \right)

HyperQB returns SAT which implies the successful finding of a qualified mutant.

Benchmarks
----------

.. tabs::

    .. tab:: Case #6.1

        **The Model(s)**

        .. tabs::

            .. tab:: Mutation Testing

                .. literalinclude :: ../models/6_mutation/mutation_testing.smv
                    :language: smv

        **Formula**

        .. literalinclude :: ../models/6_mutation/mutation_testing.hq
            :language: smv

References
----------
.. _FBW19:
- [FBW19] A. Fellner, M. Tabaei Befrouei, and G. Weissenbacher. Mutation testing with hyperproperties. In Proceedings of the 17th International Conference on Software Engineering and Formal Methods (SEFM), pages 203–221. Springer, 2019.