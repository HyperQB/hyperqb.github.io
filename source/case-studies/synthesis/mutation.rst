Synthesis for Mutation Testing (NuSMV)
========================

Description of the Case Study
-----------------------------

Another application of hyperproperties with quantifier
alternation is the efficient generation of test suites for mutation testing. We
borrow a model from :ref:`[FBW19] <FBW19>` and apply the original formula that describes a good
test mutant together with the model, expressed as:

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Mutation Testing

        .. literalinclude :: ../benchmarks_ui/nusmv/testing/mutation/mutation_testing.smv
            :language: smv

The HyperLTL formula(s)
-----------------------

The property seeks a mutant trace that diverges from the original when driven by the same inputs. HyperQB’s SAT result
identifies such a mutant, confirming the effectiveness of the generated test.

.. math::

   \varphi_{\text{mut}} = \exists \pi_A . \forall \pi_B \left(
   mut_{\pi_A} \land \neg mut_{\pi_B} \right) \land
   \left(
     \left( in_{\pi_A} \leftrightarrow in_{\pi_B} \right) \
     \mathcal{U} \
     \left( out_{\pi_A} \not\leftrightarrow out_{\pi_B} \right)
   \right)

.. tabs::

    .. tab:: Case #6.1

        .. literalinclude :: ../benchmarks_ui/nusmv/testing/mutation/mutation_testing.hq
            :language: hq

References
----------

.. _FBW19:

- [FBW19] `A. Fellner, M. Tabaei Befrouei, and G. Weissenbacher. Mutation testing with hyperproperties. In Proceedings of the 17th International Conference on Software Engineering and Formal Methods (SEFM), pages 203–221. Springer, 2019. <https://doi.org/10.1007/978-3-030-30446-1_11>`_
