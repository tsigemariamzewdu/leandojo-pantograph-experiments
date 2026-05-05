from lean_dojo import Dojo, LeanGitRepo, ProofFinished, TacticState, Theorem

repo = LeanGitRepo(
    "https://github.com/tsigemariamzewdu/lean4-example",  
    "7fba2a9b251a0af89fd999150bcd37d49ce616d9",                                
)

theorem = Theorem(repo, "Lean4Example.lean", "bar")  # repo, theorem file, theorem name

with Dojo(theorem) as (dojo, state0):
    print("Initial goal:")
    print(state0.pp)

    # Step 1: rw [add_zero] — simplifies (b + 0) to b
    state1 = dojo.run_tac(state0, "rw [add_zero]")
    print("\nAfter rw [add_zero] (step 1):")
    print(state1)

    # Step 2: rw [add_zero] — simplifies (c + 0) to c
    state2 = dojo.run_tac(state1, "rw [add_zero]")
    print("\nAfter rw [add_zero] (step 2):")
    print(state2)

    # Step 3: rfl — closes the goal
    state3 = dojo.run_tac(state2, "rfl")
    print("\nAfter rfl (step 3):")
    print(state3)

    if isinstance(state3, ProofFinished):
        print("\nSuccess: proof complete in 3 steps.")
    else:
        print("\nProof incomplete, check tactic states above.")
