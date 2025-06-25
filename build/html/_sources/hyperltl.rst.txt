HyperLTL
========

We consider hyperproperties as formulas in HyperLTL [1], which allows explicit quantification on traces. The syntax of HyperLTL formulas is defined by the following grammar:

.. math::

   \begin{array}{rcl}
   \varphi & ::= & \exists \pi . \varphi \mid \forall \pi . \varphi \mid \phi \\
   \phi    & ::= & \mathit{true} \mid a_\pi \mid \neg \phi \mid \phi \lor \phi \mid \phi \land \phi \mid \phi \mathcal{U} \phi \mid \phi \mathcal{R} \phi \mid \bigcirc \phi
   \end{array}

References
----------

1. `Temporal logics for hyperproperties. In Proceedings of the 3rd Conference on Principles of Security and Trust POST, pages 265–284, 2014. <https://arxiv.org/pdf/1401.4492>`_ *M. R. Clarkson, B. Finkbeiner, M. Koleini, K. K. Micinski, M. N. Rabe, and C. Sánchez*