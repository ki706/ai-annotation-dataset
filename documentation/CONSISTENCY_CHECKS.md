# Consistency Checks

## Purpose
This document verifies that annotation decisions follow consistent logic across the dataset.

The goal is to ensure:
- stable labeling rules
- repeatable decisions
- no random interpretation drift

---

## 1. Core Consistency Rules

### Rule A: Dominant Signal Rule
When multiple signals exist, the strongest user impact determines the label.

Examples:
- delivery delay + good product → category: delivery
- product failure + fast delivery → category: product quality

---

### Rule B: Outcome Over Intent
We prioritize final user experience, not intent.

Example:
- “support tried but failed” → negative (not neutral)

---

### Rule C: Weak Sentiment Handling
If sentiment is unclear:
- assign neutral only when no strong positive/negative signal exists

---

## 2. Repeated Pattern Consistency

### Delivery Issues
All cases with:
- delay
- missing items
- damaged packaging

→ consistently labeled as: DELIVERY (negative sentiment)

---

### Product Failure
All cases with:
- breaking
- malfunction
- poor build quality

→ consistently labeled as: PRODUCT QUALITY (negative sentiment)

---

### Customer Support Failure
All cases with:
- unresolved issue
- slow response + no solution

→ consistently labeled as: CUSTOMER SERVICE (negative sentiment)

---

## 3. Mixed Sentiment Handling

When both positive and negative appear:

- do NOT split sentiment randomly
- choose dominant experience driver

Example:
> “Product is good but delivery was bad”

→ delivery dominates → negative sentiment

---

## 4. Borderline Cases

### “Not bad”
→ Neutral

### “Okay, nothing special”
→ Neutral

### “Good but expected better”
→ Negative (expectation gap rule)

---

## 5. Consistency Validation Summary

Across dataset:
- Delivery issues consistently map to negative sentiment
- Product failures override positive delivery experience
- Support inefficiency overrides politeness
- Neutral used only for low-intensity feedback

---

## 6. Conclusion

This dataset follows a stable, rule-based annotation system designed to ensure reproducibility across different annotators.
