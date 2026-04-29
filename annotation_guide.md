# Annotation Guidelines
## Text Sentiment & Category Classification

**Project:** E-commerce Product Review Annotation
**Annotator:** Miftah Abate
**Version:** 1.0
**Last Updated:** April 2026

---

## 1. Task Overview

This document defines the rules for annotating e-commerce product reviews with:
- **Sentiment:** The overall emotional tone of the review
- **Category:** The primary topic being discussed

Every annotation decision must be traceable to a rule in this document.

---

## 2. Sentiment Labels

### 2.1 Definitions

| Label | Definition |
|---|---|
| `positive` | The reviewer is clearly satisfied. Tone is favorable. Would likely recommend or repurchase. |
| `negative` | The reviewer is clearly dissatisfied. Tone is critical. Would likely not recommend or repurchase. |
| `neutral` | The reviewer is neither clearly satisfied nor dissatisfied. Balanced or indifferent tone. |

### 2.2 Rules

**Rule S1 — Whole review, not one sentence**
Sentiment reflects the OVERALL tone of the entire review. A single positive sentence in a largely negative review does not make it positive.

**Rule S2 — Mixed reviews**
If a review contains both positive and negative elements of similar weight, label it `neutral`. Do NOT default to the first or last sentence.

**Rule S3 — Sarcasm**
If the text contains sarcasm, label based on the INTENDED meaning, not the literal words.
> Example: *"Oh great, another broken product"* → `negative`

**Rule S4 — Weak language**
Words like "fine," "okay," "decent," "not bad" typically indicate `neutral` unless surrounding context pushes clearly positive or negative.

**Rule S5 — Explicit statements**
If the reviewer explicitly states their sentiment ("mixed feelings," "neutral experience"), follow their self-description unless other signals strongly contradict it.

---

## 3. Category Labels

### 3.1 Definitions

| Label | Definition |
|---|---|
| `product_quality` | Comments about the item itself: build, materials, function, appearance, accuracy to listing |
| `delivery` | Comments about shipping speed, packaging, tracking, arrival condition |
| `customer_service` | Comments about interactions with the seller or support team |
| `price` | Comments about cost, value for money, pricing compared to alternatives |

### 3.2 Rules

**Rule C1 — Primary topic only**
Assign the category that is the PRIMARY subject of the review. If multiple topics appear, choose the one with the most content or strongest emotion.

**Rule C2 — Delivery vs. product_quality for damage**
- Damage caused DURING shipping → `delivery`
- Defect present in the product itself (before shipping) → `product_quality`

**Rule C3 — Price mentions**
If price is mentioned only as a side note ("a bit pricey but great quality") → use `product_quality`.
If price is the main complaint or praise → use `price`.

**Rule C4 — Seller communication**
Complaints about seller not responding or being rude → `customer_service`, even if it leads to a return.

---

## 4. Confidence Levels

| Level | Definition |
|---|---|
| `high` | Label is clear. Rules apply directly. No ambiguity. |
| `medium` | Some ambiguity present. Decision required judgment. Documented in annotator_notes. |
| `low` | Significant ambiguity. Edge case. Fix notes required regardless of final label. |

---

## 5. QA Process

Every item was reviewed against 4 checks after initial labeling:

1. **correct_label** — Is the label logically consistent with the review text?
2. **consistency_check** — Does this label match how similar reviews were labeled?
3. **confidence** — How clear was the decision?
4. **fix_notes** — If corrected: what was wrong, what rule applies, what the correct label is

### 5.1 Self-Correction Protocol
If initial label fails QA:
1. Identify which rule was violated
2. Apply correct rule
3. Record original label + reason for correction in fix_notes
4. Update annotated_reviews.csv with corrected label

---

## 6. Edge Case Log

| ID | Issue | Resolution |
|---|---|---|
| 9 | Unmet expectations without extreme language | Classified neutral not negative; language was mild |
| 26 | Defect present but service resolved it | Net outcome positive; customer_service is primary topic |
| 30 | Reviewer explicitly said "mixed feelings" | Respected self-description; labeled neutral despite "great" product |
| 45 | Both delivery and price mentioned negatively | Delivery was primary complaint (one month wait); price secondary |

---

## 7. What This Document Proves

A professional annotator does not just label data. They:
- Follow consistent, documented rules
- Handle edge cases with traceable decisions
- Self-correct with explanation
- Maintain a QA layer that separates first-pass from final labels

This is the difference between clickwork and professional annotation.

---

*Miftah Abate · mifab2026@gmail.com · [miftah.pages.dev/ai](https://miftah.pages.dev/ai)*
