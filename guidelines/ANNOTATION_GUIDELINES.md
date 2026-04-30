# Annotation Guidelines

## Purpose
This document defines the rules used for labeling text data in this project.

The goal is to ensure:
- consistent labeling
- clear decision rules
- repeatable interpretation across all samples

---

## 1. Labeling Structure

Each text must be labeled with:

### Sentiment
- Positive
- Negative
- Neutral

### Category
- Product Quality
- Delivery
- Customer Service
- Price / Value

### Secondary Category (optional)
Used only when:
- multiple strong signals exist
- or ambiguity cannot be resolved clearly

---

## 2. Labeling Rules

### Rule 1: Main Experience Rule
Focus on the strongest user experience in the text.

Example:
> “Good product but delivery was slow”  
→ Category: Delivery  
→ Sentiment: Negative

---

### Rule 2: Mixed Cases
If a text contains both positive and negative signals:
- prioritize the dominant issue
- do not split sentiment

---

### Rule 3: Neutral Cases
Assign Neutral when:
- no clear emotional tone exists
- or sentiment is balanced

---

## 3. Review System

Each label must include a review section:

- is_correct: true / false
- confidence_level: high / medium / low
- issue_type:
  - incorrect label
  - inconsistent decision
  - unclear meaning
  - missing context
- decision:
  - accept
  - revise
  - unclear
- notes: short explanation if needed

---

## 4. Consistency Rules

- identical patterns must have identical labels
- decisions must follow the same logic across dataset
- review system must catch inconsistencies

---

## 5. Edge Cases

### Ambiguous Text
- use Neutral if unclear
- mark confidence as low or medium

### Multi-Intent Text
- assign primary category based on strongest signal
- secondary category only if necessary

---

## 6. Quality Principles

- consistency over interpretation
- rules over intuition
- repeatability over creativity

---

## End of Guidelines
