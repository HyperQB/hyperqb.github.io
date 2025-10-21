Intermediate Representation
===========================

A key component of any `Bounded Model Checking`` (BMC) framework is the intermediate representation (IR) used to model the system under analysis. For this project, we developed an IR inspired by the NuSMV modeling language [1]_.

We chose this model for its natural ability to clearly and independently define the transition logic for each state variable. This separation simplifies the analysis pipeline, as we can reason about transitions without concern for the concrete representation of a full state. In this model, a state is simply a valuation of all system variables. The core data structure implementing this IR in our code is ``SMVEnv``, which we refer to as the environment.

The NuSMV Transition Model
--------------------------

Our IR's logic is based on NuSMV's ``case...esac`` structure for defining next-state transitions:

.. code-block:: smv

    next(variable) := case
        g1 : u1;
        g2 : u2;
        ...
        gk : uk;
        TRUE : u
    esac;

In this format, each line ``g : u;`` is a guarded transition, consisting of a boolean condition ``g`` and an update expression ``u`` (which must match the variable's type).

During a state change, the conditions are evaluated in order from top to bottom. The first condition ``g`` that holds determines the variable's next value via its corresponding update expression ``u``. If no condition holds, the ``TRUE`` branch is taken, which typically assigns the variable's current value (e.g., ``TRUE : variable;``), indicating a self-loop where no value change occurs.


The ``NuSMV`` Transition Model
------------------------------

As its name suggests, our IR is an `intermediate` representation. It is designed to be **solver-agnostic** and captures the two essential components of a state machine: the state variables and the transition logic.

The ``SMVEnv`` currently supports three variable types:

1. ``Boolean``: A boolean type, with an optional initial value.

2. ``Int``: A boundless mathematical integer, with optional initial, lower-bound, and upper-bound values.

3. ``BV``: A bit-vector type, which requires a bit-width. It can also have optional initial, lower-bound, and upper-bound values.

Defining States and Transitions
-------------------------------

Once an ``SMVEnv`` is created, new variables are added using the ``register_variable(name, type)`` method. All metadata (such as bounds or initial values) is specified within the ``type`` argument.

Transitions for a variable are defined using the ``register_transition(name, cond, upd)`` method. This method is called once for each guarded transition (like ``g: u;``) in the specific order they should be evaluated. The environment preserves this registration order, ensuring the priority logic of the NuSMV-style ``case`` statement is correctly modeled.

A key feature of our IR is that both the condition ``cond`` and the update expression ``upd`` are provided as native Rust functions. This allows for highly flexible and complex transition logic that can leverage the full power of the Rust language.

If no transitions are registered for a variable, the environment automatically assumes a self-loop (i.e., ``next(variable) := variable``).


Using Predicates
----------------

It is often necessary to check if a specific Boolean condition holds in a given state. Instead of rewriting this logic repeatedly, the IR allows you to define `predicates`.

A predicate is a named, reusable Rust boolean function that is evaluated against the current state. They are defined using the ``register_predicate(name, pred)`` method, where ``name`` is a string for future reference and pred is the boolean function. Predicates are useful for defining properties or checking for specific conditions, such as identifying a halting state in the system.

Usage
----------
As an example, consider the following simple NuSMV model, which creates a counter that goes through 0 to 15, resets to 0, and an LED that will turn on every third cycle of the counter.

.. code-block:: smv

    MODULE main
    VAR
    counter : 0..15;     -- 4-bit counter
    LED : boolean;   -- Denotes whether the LED is on

    DEFINE
    reset   := counter = 15;       -- predicate: counter about to reset
    led_blink:= (counter mod 3 = 2) | reset; -- true at counter = 2, 5, 8, 11, 14, 15

    ASSIGN
    init(counter) := 0;
    init(LED) := TRUE; -- Should blink counter = 0

    -- counter: 0..15 then reset to 0
    next(counter) := case
        reset : 0;
        TRUE : counter + 1;
    esac;

    -- Only blink if the led_blink is true
    next(LED) := case
        led_blink : TRUE;
        TRUE: FALSE;
    esac;


This model can be represented in IR as the following Rust code (imports  omitted):

.. code-block:: rust
    
    let env = SMVEnv::new(&ctx);

    env.register_variable("counter", VarType::Int {
        init: Some(vec![0]),
        lower: Some(0),
        upper: Some(15),
    });

    env.reigster_variable("LED", VarType::Bool {
        init: Some(vec![true]),
    });

    env.register_predicate("reset",
        |_env, _ctx, _state| int_var!(_state, "counter")._eq(&Int::from_i64(_ctx, 15))
    );
    env.register_predicate("led_blink",
        |_env, _ctx, _state| (int_var!(_state, "counter") % &Int::from_i64(_ctx, 3))._eq(&Int::from_i64(_ctx, 2)) | predicate!("reset", _env, _ctx, _state)
    );

    // Defining Transitions
    env.register_transition("counter",
    |_env, _ctx, _state| exact!(Node, predicate!("reset", _env, _ctx, _state)),
    |_env, _ctx, _state| exact!(Int, 0)
    );
    env.register_transition("counter",
    |_env, _ctx, _state| exact!(Bool, true),
    |_env, _ctx, _state| exact!(Node, int_var!(_state, "counter") + &Int::from_i64(_ctx, 1))
    );

    env.register_transition("LED",
    |_env, _ctx, _state| exact!(Node, predicate!("led_blink", _env, _ctx, _state))
    |_env, _ctx, _state| exact!(Bool, true)
    );
    env.register_transition("LED",
    |_env, _ctx, _state| exact!(Bool, true)
    |_env, _ctx, _state| exact!(Bool, false)
    );


References
----------

.. [1] NuSMV paper: https://nusmv.fbk.eu/papers/sttt_j/pdf/sttt_j.pdf
