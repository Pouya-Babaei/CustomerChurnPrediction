# Team Guide

## Development Philosophy

This project follows an incremental Sprint-based development methodology inspired by real-world machine learning engineering workflows.

Each Sprint focuses on a single engineering objective while maintaining reproducibility, documentation quality, and version control throughout the project lifecycle.

---

# Sprint Workflow

Each Sprint should follow the same development cycle:

1. Research & Planning
2. Implementation
3. Model Evaluation (if applicable)
4. Technical Review
5. Sprint Retrospective
6. Documentation Update
7. Git Commit & Push

---

# Coding Standards

- Follow PEP 8 guidelines.
- Use descriptive and meaningful variable names.
- Prefer reusable functions over duplicated code.
- Keep notebooks clean and organized.
- Avoid unnecessary code repetition.
- Build reusable preprocessing pipelines whenever possible.
- Use a fixed `random_state` to ensure reproducibility.
- Keep baseline models simple unless the Sprint explicitly focuses on optimization.

---

# Documentation Rules

Every completed Sprint must update the following files:

- README.md
- PROJECT_JOURNAL.md
- CHANGELOG.md
- sprint_xx.md

Documentation should include:

- Sprint Goal
- Work Completed
- Key Findings
- Lessons Learned
- Next Steps (when applicable)

---

# Model Development Rules

When implementing machine learning models:

- Keep baseline models as close to default settings as possible.
- Modify only the parameters required for reproducibility (e.g., `random_state`).
- Use the shared preprocessing pipeline across all models.
- Ensure that all models are evaluated using the same train/test split for fair comparison.
- Compare models using multiple evaluation metrics rather than Accuracy alone.

---

# Evaluation Strategy

Each classification model should be evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

Business objectives should always be considered before selecting the final model.

---

# Git Workflow

Each Sprint should conclude with:

- Documentation updates
- Git commit
- Git push

Commit messages should clearly describe the completed Sprint.

Example:

```bash
Sprint 03: Implement Logistic Regression baseline
Sprint 04: Add Decision Tree baseline
Sprint 05: Implement KNN and Gaussian Naive Bayes
```

---

# Project Principles

Throughout the project we aim to:

- Maintain reproducible experiments.
- Keep preprocessing consistent across all models.
- Compare models fairly.
- Prioritize business objectives over isolated performance metrics.
- Document every important engineering decision.