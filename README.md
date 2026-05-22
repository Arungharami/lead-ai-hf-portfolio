# 🤖 Lead.AI Labs — Hugging Face AI Portfolio

**Explainable AI Systems for Business Automation, Fraud Detection, and Predictive Intelligence**

[![Website](https://img.shields.io/badge/Website-lead--ai.us-FF6B35?style=for-the-badge)](https://www.lead-ai.us)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-arun--gharami-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/arun-gharami)
[![GitHub](https://img.shields.io/badge/GitHub-Arungharami-181717?style=for-the-badge&logo=github)](https://github.com/Arungharami)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-arunkgharami-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/arunkgharami)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge)](LICENSE)

> This repository contains all professional model cards, dataset cards, and Space metadata for the [Lead.AI Labs Hugging Face profile](https://huggingface.co/arun-gharami). Every asset is commercially framed with real business use cases, Responsible AI disclaimers, and CTAs to [lead-ai.us](https://www.lead-ai.us).

---

## 🚀 Featured Product — Lead.AI Fraud Shield

> The flagship production-ready product: a full fraud detection + XAI API built on top of this HF portfolio.

| Component | Link |
|-----------|------|
| 🛡️ GitHub Repo | [Arungharami/lead-ai-fraud-shield](https://github.com/Arungharami/lead-ai-fraud-shield) |
| 🤗 Model on HF | [arun-gharami/lead-ai-fraud-shield](https://huggingface.co/arun-gharami/lead-ai-fraud-shield) |
| 🎮 Live Demo | [fraud-detection-xai-demo](https://huggingface.co/spaces/arun-gharami/fraud-detection-xai-demo) |
| 📊 Training Data | [lead-ai-fraud-detection-dataset-v2](https://huggingface.co/datasets/arun-gharami/lead-ai-fraud-detection-dataset-v2) |
| 🏢 Business Info | [lead-ai.us](https://www.lead-ai.us) |

---

## 📦 HF Portfolio — Full Asset Map

### Models

| Model | Description | HuggingFace Link |
|-------|-------------|-----------------|
| 🛡️ **Fraud Shield** | 3-tier fraud scorer with SHAP explanation (Low/Medium/High + confidence %) | [arun-gharami/lead-ai-fraud-shield](https://huggingface.co/arun-gharami/lead-ai-fraud-shield) |
| 🔍 **Fraud Detection Model** | Binary fraud/safe classifier with risk score and plain-language reason | [arun-gharami/lead-ai-fraud-detection-model](https://huggingface.co/arun-gharami/lead-ai-fraud-detection-model) |
| 📈 **Customer Predictor** | Lead scoring / churn prediction (Hot Lead / Normal / Churn Risk) | [arun-gharami/lead-ai-customer-predictor](https://huggingface.co/arun-gharami/lead-ai-customer-predictor) |
| 💬 **Review Sentinel** | Customer review urgency scorer — catches complaints before they go public | [arun-gharami/lead-ai-review-sentinel](https://huggingface.co/arun-gharami/lead-ai-review-sentinel) |

### Datasets

| Dataset | Rows | Features | HuggingFace Link |
|---------|------|----------|-----------------|
| 📊 **Fraud Detection Dataset** | 5,000 | 14 | [arun-gharami/lead-ai-fraud-detection-dataset](https://huggingface.co/datasets/arun-gharami/lead-ai-fraud-detection-dataset) |
| 📊 **Fraud Detection Dataset v2** | 100,000 | 21 | [arun-gharami/lead-ai-fraud-detection-dataset-v2](https://huggingface.co/datasets/arun-gharami/lead-ai-fraud-detection-dataset-v2) |

### Spaces

| Space | Description | HuggingFace Link |
|-------|-------------|-----------------|
| 🎮 **Fraud Detection XAI Demo** | Live interactive fraud scorer with SHAP-style explanation | [arun-gharami/fraud-detection-xai-demo](https://huggingface.co/spaces/arun-gharami/fraud-detection-xai-demo) |

---

## 🗂️ Repository Structure

```
huggingface-portfolio/
├── profile/
│   └── README.md                           ← HF profile landing page
├── models/
│   ├── fraud-shield/README.md              ← lead-ai-fraud-shield model card
│   ├── customer-predictor/README.md        ← lead-ai-customer-predictor model card
│   ├── review-sentinel/README.md           ← lead-ai-review-sentinel model card
│   └── fraud-detection-model/README.md    ← lead-ai-fraud-detection-model card
├── datasets/
│   ├── fraud-detection-dataset/README.md   ← Dataset v1 (5K rows)
│   └── fraud-detection-dataset-v2/README.md ← Dataset v2 (100K rows)
└── spaces/
    └── fraud-detection-xai-demo/README.md  ← XAI Demo Space README
```

---

## 🔗 Cross-Platform Links

| Platform | URL |
|----------|-----|
| 🌐 Website | https://www.lead-ai.us |
| 🤗 HuggingFace | https://huggingface.co/arun-gharami |
| 🛡️ Fraud Shield Repo | https://github.com/Arungharami/lead-ai-fraud-shield |
| 🎮 Live Demo | https://huggingface.co/spaces/arun-gharami/fraud-detection-xai-demo |
| 💼 LinkedIn | https://www.linkedin.com/in/arunkgharami |

---

## ⬆️ Upload Commands

```bash
export HF_TOKEN=your_token_here   # never commit your actual token

# Profile
hf upload arun-gharami/arun-gharami profile/README.md README.md --token $HF_TOKEN

# Models
hf upload arun-gharami/lead-ai-fraud-shield models/fraud-shield/README.md README.md --token $HF_TOKEN
hf upload arun-gharami/lead-ai-customer-predictor models/customer-predictor/README.md README.md --token $HF_TOKEN
hf upload arun-gharami/lead-ai-review-sentinel models/review-sentinel/README.md README.md --token $HF_TOKEN
hf upload arun-gharami/lead-ai-fraud-detection-model models/fraud-detection-model/README.md README.md --token $HF_TOKEN

# Datasets
hf upload arun-gharami/lead-ai-fraud-detection-dataset datasets/fraud-detection-dataset/README.md README.md --repo-type dataset --token $HF_TOKEN
hf upload arun-gharami/lead-ai-fraud-detection-dataset-v2 datasets/fraud-detection-dataset-v2/README.md README.md --repo-type dataset --token $HF_TOKEN

# Space
hf upload arun-gharami/fraud-detection-xai-demo spaces/fraud-detection-xai-demo/README.md README.md --repo-type space --token $HF_TOKEN
```

---

## 🏢 About Lead.AI Labs

**Lead.AI Labs builds explainable AI, predictive analytics, fraud detection, customer intelligence, and automation systems that create measurable business value.**

> *Explainable AI Systems for Business Automation, Fraud Detection, and Predictive Intelligence.*

All models are designed to be:
- **Explainable** — decisions are traceable, auditable, and human-readable
- **Commercially deployable** — REST API, Gradio demo, Docker-ready
- **Responsibly built** — synthetic data labeled clearly, no false claims of real-world benchmarks
- **Business-first** — every output answers "what should I do next?" not just "what is the probability?"

---

## 👤 Author

**Arun Kumar Gharami**  
AI Engineer & Applied Researcher · Founder, Lead.AI Labs

[lead-ai.us](https://www.lead-ai.us) · [LinkedIn](https://www.linkedin.com/in/arunkgharami) · [GitHub](https://github.com/Arungharami) · [HuggingFace](https://huggingface.co/arun-gharami)

---

*Lead.AI Labs — Trustworthy AI Systems for Practical Business Intelligence*
