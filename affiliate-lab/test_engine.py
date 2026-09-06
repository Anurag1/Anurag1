from engine import Opportunity, expected_revenue, has_clear_disclosure, rank


ops = [
    Opportunity("AI writing tools", 0.9, 0.5, 0.4, 0.5),
    Opportunity("Generic gadgets", 0.8, 0.2, 0.9, 0.8),
]

assert rank(ops)[0].topic == "AI writing tools"
assert expected_revenue(10_000, 0.03, 0.04, 20) == 240.0
assert has_clear_disclosure(
    "I may earn a commission from purchases through these links."
)
assert not has_clear_disclosure("Best products you should buy")

print("ALL TESTS PASSED")
