from pantograph import Server

# Prove: if n is even and m is even, then n + m is even
# Evenness defined manually as ∃ k, n = 2 * k (no Mathlib needed)

with Server() as server:

    state = server.goal_start(
        "∀ (n m : Nat), (∃ k, n = 2 * k) → (∃ k, m = 2 * k) → (∃ k, n + m = 2 * k)"
    )

    print("--- Initial Goal ---")
    print(state.goals[0])

    # Introduce n, m and the two evenness hypotheses
    state = server.goal_tactic(state, tactic="intro n m hn hm")
    print("\n--- After 'intro n m hn hm' ---")
    print(state.goals[0])

    # Destructure hn into witness k with n = 2 * k
    state = server.goal_tactic(state, tactic="obtain ⟨k, hk⟩ := hn")
    print("\n--- After 'obtain ⟨k, hk⟩ := hn' ---")
    print(state.goals[0])

    # Destructure hm into witness j with m = 2 * j
    state = server.goal_tactic(state, tactic="obtain ⟨j, hj⟩ := hm")
    print("\n--- After 'obtain ⟨j, hj⟩ := hm' ---")
    print(state.goals[0])

    # Provide witness k + j: n + m = 2 * (k + j)
    state = server.goal_tactic(state, tactic="exact ⟨k + j, by rw [hk, hj]; ring⟩")
    print("\n--- After 'exact ⟨k + j, by rw [hk, hj]; ring⟩' ---")

    if not state.goals:
        print("--- Proof Finished Successfully! ---")
    else:
        print("Remaining goals:")
        for g in state.goals:
            print(g)
