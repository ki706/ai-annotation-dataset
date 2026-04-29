# Structured Text Annotation System with Quality Review Layer

## Overview
This project presents a structured text annotation dataset designed to simulate real-world data labeling workflows.

It focuses on:
- consistent labeling across noisy data
- handling ambiguous cases
- structured quality review of annotations
- rule-based decision making

---

## Objective
To build a consistent and scalable text labeling system that includes:
- sentiment classification
- category labeling
- handling mixed and ambiguous inputs
- structured review of annotation accuracy

---

## Dataset

- Total samples: 60–100 text entries
- Domain: Customer feedback

### Data Types Included:
- Clear cases (obvious sentiment and category)
- Mixed cases (multiple signals)
- Ambiguous cases (uncertain meaning)

---

## Label Structure

Each entry contains:

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
Used when a second strong signal exists.

---

## Review Fields

Each annotation includes a review section to ensure consistency and correctness:

- is_correct: true / false
- confidence_level: high / medium / low
- issue_type:
  - incorrect label
  - inconsistent labeling
  - unclear case
  - missing context
- decision:
  - accept
  - revise
  - unclear
- notes: short explanation

---

## Ambiguity Handling Rules

### Dominant Signal Rule
When multiple signals exist, choose the strongest user experience.

Example:
> “Product is good but delivery was slow”  
→ Category: Delivery  
→ Sentiment: Negative

---

### Neutral Rule
Use Neutral when:
- no clear emotional direction exists
- sentiment is balanced or unclear

---

### Secondary Category Rule
Used only when:
- two signals are equally strong
- both are important to user experience

---

## Consistency Rules

- similar cases must have similar labels
- category selection must follow defined logic
- review layer must identify inconsistencies

---

## Scalability

This framework is designed to scale to large datasets (1,000+ entries) while maintaining consistent labeling logic.

---

## Folder Structure

## Folder Structure

```bash
data-annotation-project/
│
├── data/
│   ├── raw.json
│   └── labeled.json
│
├── review/
│   └── review_log.json
│
├── guidelines/
│   └── ANNOTATION_GUIDELINES.md
│
├── scripts/
│   └── validate.py
│
└── README.md
---

## Skills Demonstrated

- structured data labeling
- consistency enforcement
- ambiguity resolution
- dataset design
- review-based validation system
- scalable annotation logic

---

## Project Status
Completed structured annotation system with review layer and ambiguity handling framework.
