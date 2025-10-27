HyperQB Manual
===================
HyperQB is a push-button, bounded model checker for verifying hyperproperties. Hyperproperties are systems-wide properties that express the behavior of system as a whole rather than the behavior of individual execution traces.

.. grid:: 2 2 2 1
   :gutter: 2

   .. grid-item-card:: Installation
      :class-card: sd-shadow-sm

      - :doc:`Overview <security/index>`

   .. grid-item-card:: Modeling Languages
      :class-card: sd-shadow-sm

      - :doc:HyperQB currently accepts input models in two languages:

         -- **NuSMV** is a symbolic BBD-based model checker originated in CMU. The full documentation of the input language is available `here <https://nusmv.fbk.eu/user-manual.html>`_.

         -- **Verilog** is a hardware description language. KEN please add a link here.

   .. grid-item-card:: Specification Languages
      :class-card: sd-shadow-sm

      - :doc:`Overview <planning/index>`

   .. grid-item-card:: Running HyperQB
      :class-card: sd-shadow-sm

      - :doc:`Overview <synthesis/index>`

.. toctree::
   :hidden:

   installation
   languages
   specs
   running
