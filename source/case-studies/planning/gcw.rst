Plan Synthesis: Wolf–Goat–Cabbage (NuSMV)
=========================================

Description of the Case Study
-----------------------------

We consider **plan synthesis (PS)** in the classic *wolf–goat–cabbage* puzzle, following . A farmer must ferry three items across a river, carrying only one at a time. Certain configurations are **unsafe** (wolf with goat, goat with cabbage) if left unattended. The goal is to synthesize a **single plan** that always avoids all local requirement violations.

This is an :math:`\exists_{\text{big}}\,\forall_{\text{small}}` problem: we search for one *big* plan that, for **every** *small* requirement automaton (encapsulating local violations), maintains safety. We provide a satisfiable instance (a robust plan exists) and an unsatisfiable one (a broken plan step that inevitably violates a requirement).

The NuSMV model(s)
------------------

.. tabs::

   .. tab:: Plan (big) — correct

      .. literalinclude::  ../benchmarks_ui/nusmv/loop_conditions/gcw/gcw1.smv
         :language: smv

   .. tab:: Requirements (small)

      .. literalinclude:: ../benchmarks_ui/nusmv/loop_conditions/gcw/gcw2.smv
         :language: smv

   .. tab:: Plan (big) — buggy

      .. literalinclude::  ../benchmarks_ui/nusmv/loop_conditions/gcw/gcw1_buggy.smv
         :language: smv

The HyperLTL formula(s)
-----------------------

The paper formulates plan synthesis as ensuring that the **plan’s action never matches any violation** of the requirement automaton, at all times:

.. math::

   \varphi_{\mathrm{PS}}
   \;=\;
   \exists \pi_{\text{big}}.\ \forall \pi_{\text{small}}'.\ 
   \mathbf{G}\,\big(\mathit{action}_{\pi_{\text{big}}} \not\leftrightarrow \mathit{violation}_{\pi_{\text{small}}'}\big).
   
In our concrete encoding, the big model exposes four violation atoms

:math:`\mathit{bad\_gc},\ \mathit{bad\_fw\_gc},\ \mathit{bad\_gw},\ \mathit{bad\_fc}`

and the small model exposes matching labels

:math:`\mathit{gc},\ \mathit{fw\_gc},\ \mathit{gw},\ \mathit{fc}`.

A pointwise version of :math:`\varphi_{\mathrm{PS}}` is:

.. math::

   \begin{aligned}
   \varphi_{\mathrm{PS}}
   \;=\;
   \exists \pi_{\text{big}}.\ \forall \pi_{\text{small}}'.\ 
   \mathbf{G}\big(&\neg(\mathit{bad\_gc}_{\pi_{\text{big}}} \land \mathit{gc}_{\pi_{\text{small}}'}) \ \land \\
                  &\neg(\mathit{bad\_fw\_gc}_{\pi_{\text{big}}} \land \mathit{fw\_gc}_{\pi_{\text{small}}'}) \ \land \\
                  &\neg(\mathit{bad\_gw}_{\pi_{\text{big}}} \land \mathit{gw}_{\pi_{\text{small}}'}) \ \land \\
                  &\neg(\mathit{bad\_fc}_{\pi_{\text{big}}} \land \mathit{fc}_{\pi_{\text{small}}'})\big).
   \end{aligned}

.. tabs::

   .. tab:: Formula

      .. literalinclude::    ../benchmarks_ui/nusmv/loop_conditions/gcw/gcw.hq
         :language: hq



References
----------

.. _RPP23:

Filiot, Emmanuel; Lagarde, Guillaume; Laroussinie, François; Markey, Nicolas; Raskin, Jean-François; and Sankur, Ocan. “Efficient Loop Conditions for Bounded Model Checking Hyperproperties.” *arXiv:2301.06209*, 2023.
