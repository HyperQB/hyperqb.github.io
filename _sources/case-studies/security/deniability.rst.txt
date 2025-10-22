Deniability (NuSMV)
===================

Description of the Case Study
-----------------------------

Deniability requires that every observable execution can be explained by multiple secrets that remain indistinguishable to an
observer. We follow Sahai, Subramanyan, and Sinha :ref:`[SSS20] <SSS20>` and the wallet examples of Backes, Köpf, and Rybalchenko
:ref:`[BKR09] <BKR09>`, checking the case :math:`N = 1` where one alternative execution suffices. In the wallet protocol, an adversary
attempts to infer the confidential balance (`sec`) by repeatedly withdrawing a fixed amount (`obs`). HyperQB verifies both a
small illustrative model and the full specification. Under the halting optimistic semantics the solver reports UNSAT, showing
that the system successfully hides the initial balance by presenting indistinguishable traces with different secrets.

The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Case #8.1

        .. literalinclude :: ../benchmarks_ui/nusmv/security/deniability/den_small.smv
            :language: smv

    .. tab:: Case #8.2

        .. literalinclude :: ../benchmarks_ui/nusmv/security/deniability/den.smv
            :language: smv

The HyperLTL formula(s)
-----------------------

The specification below states that every observable trace :math:`\pi_A` must admit two companion traces, :math:`\pi_B` and
:math:`\pi_C`, that match all observable events yet disagree on the secret. HyperQB instantiates the existential traces to
demonstrate indistinguishability or produce a counterexample if the system leaks information.

.. math::

   \begin{aligned}
   \varphi_{\text{den}} = {} & \forall \pi_A . \exists \pi_B . \exists \pi_C . \\
   & \Box \Big(
        (\mathit{obs}_{\pi_A} \leftrightarrow \mathit{obs}_{\pi_B})
        \land (\mathit{obs}_{\pi_A} \leftrightarrow \mathit{obs}_{\pi_C})
        \land (\mathit{sec}_{\pi_B} \not\leftrightarrow \mathit{sec}_{\pi_C})
     \Big)
   \end{aligned}

.. tabs::

    .. tab:: Case #8.1 & #8.2

        .. literalinclude :: ../benchmarks_ui/nusmv/security/deniability/den.hq
            :language: hq

References
----------

.. _SSS20:

- [SSS20] `S. Sahai, P. Subramanyan, and R. Sinha. Verification of quantitative hyperproperties using trace enumeration relations. In *Computer Aided Verification (CAV)*, pages 201–224, 2020. <https://doi.org/10.48550/arXiv.2005.04606>`_

.. _FHT18:

- [FHT18] `B. Finkbeiner, C. Hahn, and H. Torfah. Model checking quantitative hyperproperties. In *Computer Aided Verification (CAV)*, pages 144–163, 2018. <https://doi.org/10.1007/978-3-319-96145-3_8>`_

.. _BKR09:

- [BKR09] `M. Backes, B. Köpf, and A. Rybalchenko. Automatic discovery and quantification of information leaks. In *IEEE Symposium on Security and Privacy*, pages 141–153, 2009. <https://doi.org/10.1109/SP.2009.18>`_
