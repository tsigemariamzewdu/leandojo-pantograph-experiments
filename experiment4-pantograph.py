from pantograph import Server

# 1. Initialize the Pantograph server
with Server() as server:

    # 2. Start the proof session
    state = server.goal_start("∀ (a b c : Nat), a + (b + 0) + (c + 0) = a + b + c")

    print("--- Initial Goal ---")
    print(state.goals[0])

    # 3. Step 1: intro the variables into the context
    state = server.goal_tactic(state, tactic="intro a b c")
    print("\n--- After 'intro a b c' ---")
    print(state.goals[0])

    # 4. Step 2: First rewrite Nat.add_zero (affects b + 0)
    state = server.goal_tactic(state, tactic="rw [Nat.add_zero]")
    print("\n--- After first 'rw [Nat.add_zero]' ---")
    print(state.goals[0])

    # 5. Step 3: Second rewrite Nat.add_zero (affects c + 0)
    state = server.goal_tactic(state, tactic="rw [Nat.add_zero]")
    print("\n--- After second 'rw [Nat.add_zero]' ---")
    if state.goals:
        print(state.goals[0])
    else:
        print("\n--- Proof Finished Successfully! ---")
        exit(0)

    # 6. Step 4: Apply rfl to close the goal
    state = server.goal_tactic(state, tactic="rfl")

    if not state.goals:
        print("\n--- Proof Finished Successfully! ---")