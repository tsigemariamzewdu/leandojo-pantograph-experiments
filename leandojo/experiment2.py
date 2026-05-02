from lean_dojo import Dojo, LeanGitRepo, ProofFinished, Theorem

repo = LeanGitRepo(
    "https://github.com/yangky11/lean4-example",
    "7b6ecb9ad4829e4e73600a3329baeb3b5df8d23f",
)

# Test rewrite tactic on foo: a + 1 = a.succ
theorem = Theorem(repo, "Lean4Example.lean", "foo")

with Dojo(theorem) as (dojo, init_state):
    print("Initial goal:")
    print(init_state.pp)

    # rewrite using Nat.succ_eq_add_one in reverse to match goal
    result = dojo.run_tac(init_state, "rw [Nat.succ_eq_add_one]")
    print("\nAfter rewrite:")
    print(result)

    if isinstance(result, ProofFinished):
        print("\nSuccess: rewrite closed the goal.")
    else:
        # try finishing with rfl after rewrite
        result2 = dojo.run_tac(result, "rfl")
        print("\nAfter rfl:")
        print(result2)
        if isinstance(result2, ProofFinished):
            print("\nSuccess: rewrite + rfl closed the goal.")
