# Pantograph Experiments

These experiments use [Pantograph](https://github.com/lenianiva/PyPantograph) to interact with Lean 4 proofs via a local server interface — running tactics step by step and observing goal state transitions.

Unlike LeanDojo, Pantograph does not need a Git repo or a GitHub token. It runs Lean locally, making it faster to start with.

## Requirements

### System Dependencies

- **elan** (Lean version manager) — required to install and manage Lean 4
  ```bash
  curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh
  ```
- **git**
- **Python 3.10+**

### Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pantograph
```

> No GitHub token needed — Pantograph runs Lean locally.

## Experiments

### experiment4-pantograph.py — multi-step rewrite
Proves `∀ (a b c : Nat), a + (b + 0) + (c + 0) = a + b + c` step by step:
1. `intro a b c`
2. `rw [Nat.add_zero]` — simplifies `b + 0` to `b`
3. `rw [Nat.add_zero]` — simplifies `c + 0` to `c`
4. `rfl` — closes the goal

```bash
python3 experiment4-pantograph.py
```

Expected output:
```
--- Initial Goal ---
⊢ ∀ (a b c : Nat), a + (b + 0) + (c + 0) = a + b + c

--- After 'intro a b c' ---
a b c : Nat
⊢ a + (b + 0) + (c + 0) = a + b + c

--- After first 'rw [Nat.add_zero]' ---
a b c : Nat
⊢ a + b + (c + 0) = a + b + c

--- After second 'rw [Nat.add_zero]' ---
--- Proof Finished Successfully! ---
```

### experiment5-pantograph.py — existential proof
Proves that the sum of two even natural numbers is even, using `obtain`, `exact`, and `omega`:

```
∀ (n m : Nat), (∃ k, n = 2 * k) → (∃ k, m = 2 * k) → (∃ k, n + m = 2 * k)
```

```bash
python3 experiment5-pantograph.py
```

## How It Works

Pantograph starts a local Lean 4 server via `Server()`. `server.goal_start(statement)` initializes a proof state, and `server.goal_tactic(state, tactic=...)` applies a tactic and returns the updated state — the same `(state, tactic) → next_state` loop as LeanDojo but without needing a remote repo or tracing step.

## LeanDojo vs Pantograph

| | LeanDojo | Pantograph |
|---|---|---|
| Needs a Git repo | Yes | No |
| First run | Slow (traces repo) | Fast |
| Best for | Training data from real repos | Quick interactive proof experiments |
| GitHub token | Required | Not needed |
