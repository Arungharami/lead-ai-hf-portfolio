# Hugging Face Core Development Lab

A practical learning and contribution workspace for becoming a professional Hugging Face ecosystem developer.

## Purpose

This lab turns Hugging Face onboarding into an engineering roadmap. It combines Hub discovery, Python SDK usage, model and dataset evaluation, Space development, documentation quality, testing, and open-source contribution habits.

## Current onboarding snapshot

- Email confirmed
- Profile completed
- Follow 2 users and 1 organization completed
- Like a model, dataset, or Space: **1/3**
- Upvote an article, paper, or collection: **0/1**
- Discover products and services: **2/3**

These remaining actions are useful, but the professional goal is larger: understand how the Hugging Face Hub works and produce reproducible, documented AI assets.

## Learning outcomes

By completing this project, you will be able to:

1. Authenticate safely with the Hub without committing tokens.
2. Search and inspect models, datasets, Spaces, and papers programmatically.
3. Download and cache Hub assets.
4. run inference through supported clients.
5. Create high-quality model cards, dataset cards, and Space READMEs.
6. Build and test a small Gradio Space.
7. Use branches, issues, pull requests, and CI professionally.
8. Prepare a first contribution to a Hugging Face repository or community project.

## Eight-module roadmap

| Module | Focus | Evidence of completion |
|---|---|---|
| 01 | Account and Hub fundamentals | Profile, follows, likes, upvote, product discovery |
| 02 | CLI and authentication | `hf auth whoami`, environment check, secure token setup |
| 03 | Hub discovery API | Search script and saved JSON report |
| 04 | Models and inference | Reproducible inference notebook or script |
| 05 | Dataset engineering | Dataset inspection, schema report, data card review |
| 06 | Spaces and Gradio | Working local demo and Space-ready files |
| 07 | Quality and automation | Tests, linting, CI, documentation checks |
| 08 | Open-source contribution | Issue analysis, small patch, and pull request plan |

## Repository structure

```text
core-development/
├── README.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── pyproject.toml
├── .env.example
├── src/
│   └── hub_discovery.py
├── tests/
│   └── test_hub_discovery.py
├── reports/
│   └── .gitkeep
└── docs/
    └── onboarding-checklist.md
```

## Quick start

```bash
cd core-development
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

Authenticate using the current `hf` CLI:

```bash
hf auth login
hf auth whoami
```

Never commit your Hugging Face token. Use an environment variable when automation needs one:

```bash
cp .env.example .env
export HF_TOKEN="your_token_here"
```

Run the discovery report:

```bash
python -m src.hub_discovery --query "explainable AI" --limit 5 --output reports/discovery.json
```

Run quality checks:

```bash
ruff check .
pytest
```

## Professional development rules

- Every experiment must state its purpose, input, output, and limitations.
- Every model must have a model card.
- Every dataset must document its source, license, intended use, and risks.
- Every Space must include a clear user flow and responsible-use notice.
- Every change should be made on a branch and reviewed through a pull request.
- Never describe synthetic or demonstration results as production validation.

## Recommended first portfolio milestone

Build one complete vertical slice:

1. Select a trustworthy or explainable AI model.
2. Inspect an appropriate public dataset.
3. Run a reproducible inference example.
4. Create a small Gradio interface.
5. Publish documentation describing limitations and intended use.
6. Link the model, dataset, Space, GitHub repository, and research note together.

For Arun's portfolio, the best first vertical slice is **Explainable Fraud Risk Analysis**, because it connects existing Lead.AI work with professional Hub engineering practices.

## Definition of done

The lab is complete when:

- All onboarding actions show complete.
- The discovery script and tests pass.
- At least one model, dataset, and Space have been technically reviewed.
- One Space is reproducible locally.
- CI validates formatting and tests.
- A contribution candidate is documented with repository, issue, scope, and validation plan.
