---
title: Fraud Detection XAI Demo
emoji: 🛡️
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: true
license: apache-2.0
short_description: Transaction fraud risk scorer with XAI explanations
tags:
- fraud-detection
- explainable-ai
- xai
- shap
- tabular-classification
- trustworthy-ai
- lead-ai-labs
---

# 🛡️ Fraud Detection XAI Demo

### See the AI Decision AND the Reason — Live, in Your Browser

[![Commission a Custom Build](https://img.shields.io/badge/Deploy%20for%20Your%20Business-lead--ai.us-FF6B35?style=for-the-badge)](https://www.lead-ai.us)
[![Connect on LinkedIn](https://img.shields.io/badge/Work%20With%20Me-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/arunkgharami)

> Built by [Arun Kumar Gharami](https://huggingface.co/arun-gharami) · [Lead.AI Labs](https://www.lead-ai.us)

---

## What This Demo Does

Most fraud AI demos show you a number. This one shows you **the number and the reason**.

Enter any transaction using the sliders and dropdowns. Click **Analyze Transaction**.
In seconds you get:

- ✅ A **risk label** — Low Risk / Medium Risk / High Risk
- ✅ A **confidence score** — how certain the model is
- ✅ A **plain-English explanation** — which features drove the decision and why

This is exactly what a real fraud triage system should give your analysts: not just a flag,
but the reasoning that makes the flag actionable and defensible.

---

## Try This Scenario

Set these values and hit Analyze:

| Input | Value | Why |
|-------|-------|-----|
| Transaction Amount | $1,200 | Above normal |
| Transaction Hour | 1 AM | Off-hours |
| Payment Method | Crypto | Hard to reverse |
| Account Age | 8 days | Brand new account |
| Previous Orders | 0 | No history |
| Device Risk Score | 0.91 | High-risk device |
| Merchant Risk Score | 0.82 | High-risk merchant |

**Expected result:** High Risk · ~94% confidence · Explanation: device score, new account, crypto method

---

## Why Explainability Is the Differentiator

Any model can output "Fraud." The question is: *why?*

Without an explanation:
- Your analyst spends 5–10 minutes investigating the raw transaction data
- Your customer can't understand why their payment was declined
- Your compliance team has no audit trail

With Lead.AI XAI:
- The reason is in the output — investigation time drops to seconds
- Customer communication is specific: *"Your payment was flagged because of your device and account age"*
- Every decision is logged and explainable for regulatory review

---

## Inputs

| Input | Type | Range |
|-------|------|-------|
| Transaction Amount | Slider | $0 – $10,000 |
| Transaction Hour | Slider | 0–23 |
| Payment Method | Dropdown | crypto / card / bank transfer |
| Customer Age | Slider | 18–80 |
| Account Age (days) | Slider | 1–3,650 |
| Previous Orders | Slider | 0–500 |
| Merchant Risk Score | Slider | 0.0–1.0 |
| Device Risk Score | Slider | 0.0–1.0 |
| Location Risk Score | Slider | 0.0–1.0 |

## Outputs

| Output | Description |
|--------|-------------|
| Risk Label | Low / Medium / High Risk |
| Confidence | Model probability (0–100%) |
| Explanation | Top 3 risk drivers in plain English |

---

## Like What You See?

This demo runs on a model trained with **synthetic data** as a proof of concept.

For your business, Lead.AI Labs builds the same system retrained on your real transaction
data — tuned to your specific fraud patterns, integrated into your payment stack, and
deployable in days, not months.

**What a production engagement includes:**
- ✅ Model retrained on your transaction history
- ✅ Tuned thresholds for your false-positive tolerance
- ✅ REST API with authentication and logging
- ✅ Live monitoring dashboard
- ✅ Ongoing model refresh as fraud patterns evolve

**→ [Start a conversation at lead-ai.us](https://www.lead-ai.us)**  
**→ [Connect on LinkedIn](https://www.linkedin.com/in/arunkgharami)**

---

## ⚠️ Responsible AI Notice

> This demo uses a model trained on **synthetic data only**.
> It is for **educational and demonstration purposes** — not for production fraud enforcement.
> Do not use outputs from this demo to make real decisions about real transactions or customers.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| ML Model | scikit-learn — Gradient Boosting / Random Forest |
| Explainability | SHAP-style feature attribution |
| Interface | Gradio |
| Data | Lead.AI synthetic fraud dataset (100K rows) |
| Hosting | Hugging Face Spaces |

---

## Related Assets

| Asset | Link |
|-------|------|
| 🛡️ Fraud Shield (3-tier scorer) | [arun-gharami/lead-ai-fraud-shield](https://huggingface.co/arun-gharami/lead-ai-fraud-shield) |
| 🔍 Fraud Detection Model (binary) | [arun-gharami/lead-ai-fraud-detection-model](https://huggingface.co/arun-gharami/lead-ai-fraud-detection-model) |
| 📊 Dataset v1 (5K) | [lead-ai-fraud-detection-dataset](https://huggingface.co/datasets/arun-gharami/lead-ai-fraud-detection-dataset) |
| 📊 Dataset v2 (100K) | [lead-ai-fraud-detection-dataset-v2](https://huggingface.co/datasets/arun-gharami/lead-ai-fraud-detection-dataset-v2) |

---

*Lead.AI Labs — Trustworthy AI Systems for Practical Business Intelligence*  
[lead-ai.us](https://www.lead-ai.us) · [LinkedIn](https://www.linkedin.com/in/arunkgharami) · [GitHub](https://github.com/Arungharami)
