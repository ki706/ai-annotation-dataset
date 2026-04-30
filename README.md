# Structured Text Annotation System

## Overview

This repository contains a structured text annotation dataset designed to simulate real-world data labeling workflows with ambiguity, conflicting signals, and decision-based labeling logic.

The system reflects production-style annotation where consistency, rules, and validation are critical.

---

## Key Features

- Multi-class text annotation (sentiment + category)
- Ambiguity-aware labeling system
- Rule-based decision framework
- Consistency enforcement across dataset
- Annotation correction tracking
- Lightweight validation script for data integrity

---

## Problem This Project Solves

Real-world text data is often:
- ambiguous
- inconsistent
- noisy
- context-dependent

This project demonstrates how to structure annotation logic so that:
- different annotators produce consistent results
- labeling decisions follow repeatable rules
- dataset quality can be validated programmatically

---

## Dataset Structure
```bash

data/
├── raw.json        # Original unprocessed text samples
├── labeled.json    # Structured annotations with labels + review fields
```

---

## Annotation Framework

### Sentiment Classes
- positive
- negative
- neutral

### Categories
- product quality
- delivery
- customer service
- price/value

### Decision Principle

All labeling decisions follow a single rule:

> The dominant user experience determines the final label.

---

## Handling Ambiguity

When multiple signals exist:

- prioritize strongest user impact
- avoid splitting sentiment incorrectly
- use secondary category only when necessary

---


## Quality Control System

This dataset includes structured review tracking:

- validation of annotation consistency
- detection of ambiguous cases
- correction history logging
- confidence level tracking

---

## Validation Tool

A lightweight Python script ensures dataset integrity.

It checks:
- missing fields
- invalid sentiment values
- duplicate IDs
- empty text entries

Run:

```bash
python scripts/validate.py
