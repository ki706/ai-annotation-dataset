
# Corrections Log

## Purpose
This document records annotation corrections made during review.

It demonstrates:
- ability to identify labeling mistakes
- consistency enforcement
- improvement of annotation quality over time

---

## 1. Correction Format

Each correction follows:

- Original label
- Corrected label
- Reason for change

---

## 2. Corrections

### Case 1
**ID:** 8  
**Text:** Delivery was fast, but I’m satisfied with the product

- Before:
  sentiment: positive ❌

- After:
  sentiment: negative ✔  
  category: delivery

- Reason:
  Delivery issue has stronger impact than product satisfaction

---

### Case 2
**ID:** 35  
**Text:** Arrived late, but the product exceeded my expectations

- Before:
  sentiment: positive ❌

- After:
  sentiment: negative ✔  
  category: delivery

- Reason:
  Delivery delay affects overall experience more strongly

---

### Case 3
**ID:** 28  
**Text:** Good value for money, but build quality is average

- Before:
  sentiment: positive ❌

- After:
  sentiment: neutral ✔  
  category: product quality + price (secondary)

- Reason:
  Mixed sentiment balances out → neutral classification

---

### Case 4
**ID:** 41  
**Text:** The item arrived damaged, but replacement was quick

- Before:
  category: customer service ❌

- After:
  category: delivery ✔  
  sentiment: negative

- Reason:
  Root issue is product condition, not service response

---

### Case 5
**ID:** 57  
**Text:** The product performs well, but shipping took too long

- Before:
  sentiment: positive ❌

- After:
  sentiment: negative ✔  
  category: delivery

- Reason:
  Delivery delay dominates final user experience

---

## 3. Key Correction Patterns

### Pattern A: Delivery Dominance
Delivery issues frequently override positive product sentiment.

---

### Pattern B: Outcome Priority
Final user experience always outweighs partial positives.

---

### Pattern C: Category Fixes
Some cases required category correction due to misidentification of root cause.

---

## 4. Summary

Corrections improve dataset consistency by enforcing:
- dominant signal logic
- stable category mapping
- realistic annotation behavior
