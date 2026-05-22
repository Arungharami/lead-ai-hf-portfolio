---
license: mit
language:
- en
tags:
- fraud-detection
- binary-classification
- tabular-classification
- explainable-ai
- xai
- trustworthy-ai
- responsible-ai
- finance
- scikit-learn
- lead-ai-labs
- synthetic-data
pipeline_tag: tabular-classification
library_name: sklearn
---

# 🔍 Lead.AI Fraud Detection Model

### Binary Fraud / Safe Classifier with Risk Score and Plain-Language Explanation

[![Try Live Demo](https://img.shields.io/badge/Try%20Live%20Demo-Fraud%20XAI%20Space-blue?style=for-the-badge)](https://huggingface.co/spaces/arun-gharami/fraud-detection-xai-demo)
[![Deploy via Lead.AI Labs](https://img.shields.io/badge/Deploy%20This%20Model-lead--ai.us-FF6B35?style=for-the-badge)](https://www.lead-ai.us)
[![Contact](https://img.shields.io/badge/Commission%20Custom%20Build-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/arunkgharami)

> Built by [Arun Kumar Gharami](https://huggingface.co/arun-gharami) · [Lead.AI Labs](https://www.lead-ai.us)

---

## The Business Problem This Solves

Your payment stack processes transactions in milliseconds. Fraudulent ones look identical
to legitimate ones — until the chargeback arrives weeks later. By then you've shipped the
goods, paid the processing fee, and absorbed the dispute cost.

**This model scores every transaction as Fraud or Safe in real time, with a risk probability
and a human-readable reason** — so your team knows not just *what* to block, but *why*.

---

## What It Returns

```json
{
  "prediction": "Fraud",
  "risk_score": 0.91,
  "explanation": "High transaction velocity in the past hour, new account, and international flag are the primary risk drivers."
}
```

| Output | Values | Business meaning |
|--------|--------|-----------------|
| `prediction` | `Fraud` / `Safe` | Binary routing decision |
| `risk_score` | 0.0–1.0 | Tune your own threshold — e.g. >0.7 = manual review |
| `explanation` | Plain English | Audit trail for disputes, compliance, chargebacks |

> Need three risk tiers instead of binary? See the extended
> [Lead.AI Fraud Shield](https://huggingface.co/arun-gharami/lead-ai-fraud-shield)
> (Low / Medium / High with confidence score).

---

## Who Should Use This

| Business Type | Use Case |
|--------------|----------|
| Banks & credit unions | Real-time transaction monitoring |
| Lending platforms | Application and disbursement fraud |
| Fintech startups | Fraud layer before you can afford a dedicated risk team |
| Internal risk / ops | First-pass automated triage before analyst review |
| Researchers | Baseline binary fraud classifier for benchmarking |

---

## Input Features

| Feature | Type | Description |
|---------|------|-------------|
| `transaction_amount` | float | Transaction value |
| `transaction_hour` | int | Hour of day (0–23) |
| `account_age_days` | int | Days since account creation |
| `previous_chargebacks` | int | Historical chargeback count |
| `transaction_velocity_1h` | int | Transactions in last 1 hour |
| `transaction_velocity_24h` | int | Transactions in last 24 hours |
| `is_international` | int | 1 = international transaction |
| `is_high_risk_merchant` | int | 1 = high-risk merchant category |
| `customer_risk_score` | float | Aggregated customer risk (0.0–1.0) |

---

## Integration Example

```python
import joblib
import pandas as pd

model = joblib.load("model/model.joblib")

txn = pd.DataFrame([{
    "transaction_amount": 850.0,
    "transaction_hour": 2,
    "account_age_days": 12,
    "previous_chargebacks": 2,
    "transaction_velocity_1h": 5,
    "transaction_velocity_24h": 18,
    "is_international": 1,
    "is_high_risk_merchant": 1,
    "customer_risk_score": 0.87
}])

label = model.predict(txn)           # "Fraud"
score = model.predict_proba(txn)     # [[0.09, 0.91]]
```

**Integration time:** ~2 hours for a developer familiar with Python REST APIs.

---

## Live Demo

**Don't take our word for it — try it yourself:**

🖥️ **[Fraud Detection XAI Demo →](https://huggingface.co/spaces/arun-gharami/fraud-detection-xai-demo)**

Adjust sliders, submit a transaction, and see the fraud/safe decision with a live explanation.
Share the demo link directly with stakeholders who need to approve the AI budget.

---

## Explainability — the Feature That Closes Disputes

Most fraud models are black boxes. This one tells you *why* it flagged a transaction.

That matters for three reasons:
1. **Disputes:** "The transaction was flagged because of high velocity, new account, and international origin" is a defensible audit trail
2. **Analyst efficiency:** Reviewers who see a reason take 60–80% less time per decision
3. **Compliance:** Financial regulators increasingly expect decision transparency for automated systems

---

## Deployment Options

| Option | Description | Time |
|--------|-------------|------|
| **Python direct** | `joblib.load()` + your API wrapper | ~2 hours |
| **Gradio demo** | Run `app.py` for a visual interface | ~30 min |
| **FastAPI wrapper** | See `sample_api_usage.py` | ~1 day |
| **Production custom build** | Retrained on your data, your infra | [Contact us](https://www.lead-ai.us) |

---

## Want This in Production?

- ✅ Retrained on **your actual transaction history**
- ✅ Threshold tuning matched to your chargeback tolerance
- ✅ REST API with authentication, rate limiting, and logging
- ✅ Integration with Stripe, Braintree, Adyen, or custom payment stack
- ✅ Live monitoring dashboard with fraud rate trends
- ✅ Monthly model refresh as fraud patterns evolve

**→ [Commission a custom build at lead-ai.us](https://www.lead-ai.us)**  
**→ [Connect on LinkedIn](https://www.linkedin.com/in/arunkgharami)**

---

## Responsible AI & Limitations

- Trained on synthetic data — real-world validation required before production use
- No regulatory certification (FFIEC, PCI-DSS, GDPR, etc.)
- Must not be used as the sole basis for fraud enforcement without human review
- False positive rate must be tuned per business — defaults are not production-ready

---

## Related Assets

| Asset | Description |
|-------|-------------|
| [Lead.AI Fraud Shield](https://huggingface.co/arun-gharami/lead-ai-fraud-shield) | Extended 3-tier scorer with confidence % |
| [Fraud Dataset v2 (100K)](https://huggingface.co/datasets/arun-gharami/lead-ai-fraud-detection-dataset-v2) | Training data — 21 features, 100K rows |
| [XAI Demo Space](https://huggingface.co/spaces/arun-gharami/fraud-detection-xai-demo) | Live interactive demo |

---

## Citation

```bibtex
@misc{gharami2024frauddetection,
  author       = {Arun Kumar Gharami},
  title        = {Lead.AI Fraud Detection Model: Binary Transaction Fraud Classifier with XAI},
  year         = {2024},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/arun-gharami/lead-ai-fraud-detection-model}}
}
```

---

## License

MIT — Free to use. For a production deployment with support SLA, contact [lead-ai.us](https://www.lead-ai.us).

---

*Lead.AI Labs — Trustworthy AI Systems for Practical Business Intelligence*  
[lead-ai.us](https://www.lead-ai.us) · [LinkedIn](https://www.linkedin.com/in/arunkgharami) · [GitHub](https://github.com/Arungharami)
