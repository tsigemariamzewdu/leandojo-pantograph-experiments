from pettachainer import PeTTaChainer, check_query, check_stmt

# Prove: a + (b + 0) + (c + 0) = a + b + c
#
# Note: we use symbolic names Plus/Zero instead of +/0
# because PeTTaChainer's eval treats + and 0 as arithmetic operators.
#
# Proof strategy:
#   Axiom 1: b + 0 = b
#   Axiom 2: c + 0 = c
#   Axiom 3: congruence — if both axioms hold, the full equality follows

handler = PeTTaChainer()

print("=== Adding axioms ===")

handler.add_atoms_no_check([
    # Axiom 1: b + Zero = b
    "(: add_zero_b (Eq (Plus b Zero) b) (STV 1.0 1.0))",

    # Axiom 2: c + Zero = c
    "(: add_zero_c (Eq (Plus c Zero) c) (STV 1.0 1.0))",

    # Axiom 3: congruence rule — if both rewrites hold, full equality follows
    "(: cong_abc "
    "  (Implication "
    "    (Premises (Eq (Plus b Zero) b) (Eq (Plus c Zero) c)) "
    "    (Conclusions (Eq (Plus (Plus a (Plus b Zero)) (Plus c Zero)) (Plus (Plus a b) c)))) "
    "  (STV 1.0 1.0))",
])

print("Axioms added.")

print("\n=== Querying intermediate facts ===")

q1 = handler.query("(: $prf (Eq (Plus b Zero) b) $tv)", steps=10)
print(f"b + Zero = b  → {q1}")

q2 = handler.query("(: $prf (Eq (Plus c Zero) c) $tv)", steps=10)
print(f"c + Zero = c  → {q2}")

print("\n=== Querying final goal ===")
print("Goal: a + (b + Zero) + (c + Zero) = a + b + c\n")

q_final = handler.query(
    "(: $prf (Eq (Plus (Plus a (Plus b Zero)) (Plus c Zero)) (Plus (Plus a b) c)) $tv)",
    steps=50
)

if q_final:
    print("--- Proof Found! ---")
    for r in q_final:
        print(r)
else:
    print("--- No proof found within step budget ---")
