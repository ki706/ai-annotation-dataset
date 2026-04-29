# Text Data Annotation Project

## Overview
This project contains a structured text dataset annotated for sentiment analysis and category classification.  
The goal is to demonstrate consistent data labeling, rule-following, and basic quality assurance (QA) practices commonly used in AI training data pipelines.

---

## Objective
To simulate a real-world data annotation workflow by:
- Labeling customer feedback texts
- Assigning sentiment categories
- Classifying feedback types
- Performing basic QA validation for consistency and correctness

---

## Dataset Description

- Total samples: 50
- Data type: Customer feedback text
- Sources: Synthetic / manually created realistic examples

---

## Labeling Schema

Each data entry includes:

### 1. Sentiment
- Positive
- Negative
- Neutral

### 2. Category
- Product Quality
- Delivery
- Customer Service
- Price / Value

---

## Example Annotation

```json
{
  "text": "Delivery was late and package was damaged",
  "sentiment": "negative",
  "category": "delivery",
  "qa": {
    "correct_label": true,
    "confidence": "high",
    "notes": "Clear delivery issue and negative sentiment"
  }
}
