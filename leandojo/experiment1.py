from lean_dojo import Dojo, LeanGitRepo, ProofFinished, Theorem

# Minimal setup: use a tiny Lean repo from LeanDojo docs.
# This avoids downloading/tracing all of mathlib for a first rfl experiment.
repo = LeanGitRepo(
    "https://github.com/yangky11/lean4-example",
    "7b6ecb9ad4829e4e73600a3329baeb3b5df8d23f",
)

# theorem foo (a : Nat) : a + 1 = Nat.succ a := by rfl
theorem = Theorem(repo, "Lean4Example.lean", "foo")

with Dojo(theorem) as (dojo, init_state):
    print("Initial goal:")
    print(init_state.pp)

    result = dojo.run_tac(init_state, "rfl")
    print("\nAfter tactic rfl:")
    print(result)

    if isinstance(result, ProofFinished):
        print("\nSuccess: rfl closed the goal.")
    else:
        print("\nThe tactic did not finish the proof.")