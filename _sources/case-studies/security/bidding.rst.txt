Non-Interference Until Close: Secure Winner Disclosure in Fixed-Bid Auctions (NuSMV)
===================================

Description of the Case Study
-----------------------------

In this case study, we model a real-world bidding system adopted from [Arden12]_. The bidding service accepts a fixed, predetermined number of bids during an active bidding phase. All bids are processed and compared internally, and no user-visible indication of the winner, or any information that could allow users to infer the winner, is released before the bidding phase ends and all bids have been received.

The intended security requirement is a simplified non-interference property with declassification at the moment the auction closes. Concretely, throughout the bidding phase the observable outputs must be independent of the bid values (no premature leakage); only when the auction ends is a single piece of information, the final winner, declassified and made observable. This ensures that intermediate outputs cannot influence participant behavior or reveal partial outcomes, while still allowing the correct winner to be announced once the process is complete.

This case study evaluates four versions: three are satisfiable and one is unsatisfiable.



The NuSMV model(s)
------------------

.. tabs::

    .. tab:: Bidding V1 - Safe

        .. literalinclude :: ../benchmarks_ui/nusmv/security/bidding/bid_safe.smv
            :language: smv

    .. tab:: Bidding V2 - Safe

        .. literalinclude :: ../benchmarks_ui/nusmv/security/bidding/bid_safe_2.smv
            :language: smv

    .. tab:: Bidding V3 - Safe

        .. literalinclude :: ../benchmarks_ui/nusmv/security/bidding/bid_safe_4.smv
            :language: smv

    .. tab:: Bidding V4 - Unsafe

        .. literalinclude :: ../benchmarks_ui/nusmv/security/bidding/bid_unsafe.smv
            :language: smv

The HyperLTL formula
--------------------

This requirement can be specified as simplified non-interference with declassification (NI-D) as follows:

.. math::

   \varphi_{bid}^{\text{NI-D}} = \forall \pi_1.\forall \pi_2.\ \Box\left( \mathit{winner}_{\pi_1} = \mathit{winner}_{\pi_2} \right) \mathbin{\mathbf{W}} \#_{\pi_1}

.. tabs::

    .. tab:: Case Bidding

        .. literalinclude :: ../benchmarks_ui/nusmv/security/bidding/bidding.hq
            :language: hq

References
----------
.. [Arden12] `O. Arden, M. D. George, J. Liu, K. Vikram, A. Askarov, and A. C. Myers. Sharing Mobile Code Securely with Information Flow Control. Proceedings of the 2012 IEEE Symposium on Security and Privacy (SP '12), 191–205. IEEE Computer Society, 2012. <https://doi.org/10.1109/SP.2012.22>`_