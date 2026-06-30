"""
================================================================================
PHASE 6 — INSIGHT GENERATION
================================================================================
Goal: Turn numbers into ACTION. Numbers and charts are NOT insights — they must
be interpreted.

The Day 6 "Insight Ladder":

   OBSERVATION    -> a raw fact from the data
        |            "Electronics total revenue is the highest."
        v
   FINDING        -> a confirmed, contextualized fact
        |            "Electronics earns most DESPITE fewer units sold."
        v
   INSIGHT        -> what it MEANS for the business (the 'aha')
        |            "Revenue depends on a few high-value Electronics sales."
        v
   RECOMMENDATION -> what to DO about it (this is the value)
                     "Prioritize Electronics stock; protect against stockouts."

This file PRINTS the ladder for each finding so students see the climb.
================================================================================
"""

# Each row models one climb up the ladder. A beginner stops at the first column.
# A professional reaches the last column.
ladder = [
    {
        "observation":    "Electronics has the highest total revenue.",
        "finding":        "Electronics earns the most despite selling few units.",
        "insight":        "Revenue is concentrated in high-value Electronics.",
        "recommendation": "Prioritize Electronics inventory and prevent stockouts.",
    },
    {
        "observation":    "Pune has the most orders.",
        "finding":        "Pune leads in both order count and revenue.",
        "insight":        "Pune is the strongest market.",
        "recommendation": "Increase marketing investment in Pune.",
    },
    {
        "observation":    "Grocery has high quantities but low amounts.",
        "finding":        "Grocery drives volume, not revenue.",
        "insight":        "Grocery attracts footfall but earns little per order.",
        "recommendation": "Use Grocery to attract customers, then upsell Electronics.",
    },
    {
        "observation":    "One order was recorded as 999999 (now fixed).",
        "finding":        "A data-entry error existed in the source data.",
        "insight":        "Data-quality controls at entry are weak.",
        "recommendation": "Add input validation to prevent bad entries.",
    },
]

print("=" * 70)
print("THE INSIGHT LADDER  (Observation -> Finding -> Insight -> Recommendation)")
print("=" * 70)

for i, step in enumerate(ladder, start=1):
    print(f"\n--- Climb #{i} ---")
    print(f"  OBSERVATION    : {step['observation']}")
    print(f"  FINDING        : {step['finding']}")
    print(f"  INSIGHT        : {step['insight']}")
    print(f"  RECOMMENDATION : {step['recommendation']}")

print("""
----------------------------------------------------------------------
WHY THIS PHASE MATTERS
A beginner stops at OBSERVATIONS ("Electronics revenue is highest").
A professional climbs to RECOMMENDATIONS ("Prioritize Electronics stock").
Always answer the decision-maker's silent question: "So what should we do?"
----------------------------------------------------------------------
""")
