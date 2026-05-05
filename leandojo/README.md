# LeanDojo Experiments

These experiments use [LeanDojo](https://github.com/lean-dojo/LeanDojo) to interact with Lean 4 proofs programmatically — running tactics step by step and observing goal state transitions.

## Requirements

### System Dependencies

- **elan** (Lean version manager) — required by LeanDojo to manage Lean toolchains
  ```bash
  curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh
  ```
- **git**
- **Python 3.10+**

### Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install lean-dojo
```

### Environment Variables

A GitHub personal access token is required to avoid API rate limits when LeanDojo fetches repo metadata:

```bash
export GITHUB_ACCESS_TOKEN=<your_token>
```

Generate one at: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic), with `repo` scope.

## Experiments

### experiment1.py — `rfl` tactic
Proves `foo : a + 1 = a.succ` using `rfl` on the [lean4-example](https://github.com/yangky11/lean4-example) repo.

```bash
python3 experiment1.py
```

Expected output:
```
Initial goal:
a : Nat
⊢ a + 1 = a.succ

After tactic rfl:
ProofFinished(tactic_state_id=1, message='')

Success: rfl closed the goal.
```

### experiment2.py — `rewrite` tactic
Proves the same theorem using `rw [Nat.succ_eq_add_one]` followed by `rfl`, testing the rewrite tactic.

```bash
python3 experiment2.py
```

### experiment3.py — multi-step rewrite
Proves `bar : a + (b + 0) + (c + 0) = a + b + c` using two `rw [add_zero]` steps then `rfl`.
Uses a fork of lean4-example with the `bar` theorem added.

```bash
python3 experiment3.py
```

> Note: First run traces the repo and takes several minutes. You will see Ray launching (`Started a local Ray instance`) — this is normal, LeanDojo uses Ray internally for parallelism.
>
> If you get a `FileNotFoundError` about `.ast.json`, the cache is corrupted. Clear it and retry:
> ```bash
> rm -rf ~/.cache/lean_dojo
> python3 experiment3.py
> ```

## How It Works

LeanDojo launches a Lean process and exposes a `Dojo` context manager. Inside it, `dojo.run_tac(state, tactic)` applies a tactic and returns the next proof state — the core `(state, tactic) → next_state` loop used for GNN tactic prediction.

