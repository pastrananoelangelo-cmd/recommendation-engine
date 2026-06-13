# Mini Recommendation Engine

## Overview
A recommendation system built from scratch to understand how real-world recommender systems work under the hood.

The project starts with traditional algorithmic approaches and gradually evolves toward machine learning concepts.

The goal is to understand:
- How user behavior becomes structured data
- How relationships between items are discovered
- How recommendation scores are computed
- How bias (popularity) affects recommendations
- How systems explain why something is recommended
- How recommendation systems evolve into machine learning models


## Project Goals

### Phase 1 - Data Understanding
- Create and process user interaction data
- Represent user behavior using Python data structures
- Understand how raw data becomes usable information


### Phase 2 - Recommendation Algorithm
Implement a recommendation engine using:

- Item co-occurrence graph
- Frequency-based relationship weights
- Normalized item-to-item connections


Example:

If users frequently interact with:

Keyboard → Mouse

then the system learns:

Users interested in Keyboard may also like Mouse.


### Phase 3 - Improving Recommendations

Enhance recommendations using:

- Weighted scoring based on user preferences
- Top-K recommendations
- Popularity bias reduction (to avoid over-recommending common items)
- Normalized graph weights


### Phase 4 — Explainable Recommendations (V1 Feature)

A key feature of this system is interpretability.

Each recommendation includes:

- Final score (ranking strength)
- Contribution breakdown (what influenced the recommendation)
- Human-readable explanation (“Why this was recommended”)

Example:

Recommended because it is mainly influenced by Laptop usage, with additional influence from Mouse.


### Phase 5 - Machine Learning Bridge

Extend the system toward ML concepts:

- Feature engineering from interaction data
- Training datasets from user-item behavior
- Prediction modeling
- Evaluation metrics (precision, recall, ranking quality)


## PERSONAL GOAL

To understand:

- Build a system that teaches me why machine learning exists in the first place.
- Why machine learning is needed in recommendation systems, and what problems it solves beyond rule-based and graph-based approaches.


## Technologies

- Python
- Data structures / Graoh structures
- Algorithms (ranking, traversal, sorting)
- Basic statistics (normalization, frequency, probability)


## Current Version

Version 1.0 — Graph-Based Explainable Recommender System

A fully working recommendation engine implemented without machine learning libraries to understand the underlying logic.

Features:

- Item-to-item graph construction
- Normalized relationship weights
- User preference weighting
- Popularity bias correction
- Top-K recommendation ranking
- Explainable recommendations (Why + Evidence breakdown)

## Example Output
Recommended: Monitor

Why: This is mainly influenced by Laptop usage, with additional influence from Mouse.

Evidence:

    - Laptop: 66.67%

    - Mouse: 33.33%

Score: 0.2165

## What This Project Demonstrates
- Ability to design a full data pipeline from scratch
- Understanding of graph-based recommendation systems
- Awareness of bias in ranking systems
- Early-stage explainable AI thinking
- Strong foundation for machine learning transition