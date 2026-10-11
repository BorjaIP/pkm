---
title:  Privacy Enhancing Technologies & Benefits
created: Friday 11th April 2025 23:11
aliases: 
tags:
  - pet
  - security
  - ml
---
- https://research.aimultiple.com/privacy-enhancing-technologies/
- Type: reference
- Source: AIMultiple · Cem Dilmegani (updated 2026)

---

# TL;DR

An overview of 11 **privacy-enhancing technologies**, with a definition, benefits, example and limits for each, aimed at regulatory compliance and safe data sharing.

# What it covers

[[PET]]s protect data using cryptography, anonymisation and obfuscation, helping with GDPR/CCPA compliance, secure sharing with third parties and lower breach risk. The article lists homomorphic encryption, secure multi-party computation, differential privacy, zero-knowledge proofs, trusted execution environments, obfuscation, pseudonymisation, data minimisation, communication anonymisers, synthetic data and federated learning.

# Key takeaways

1. **Compute on protected data**: homomorphic encryption (third party computes on ciphertext) and SMPC (parties jointly compute without exposing inputs).
2. **Add noise**: differential privacy gives a formal, quantifiable guarantee for group statistics.
3. **Prove without revealing**: zero-knowledge proofs, e.g. age verification in a wallet app.
4. **Isolate hardware**: TEEs run sensitive code in a protected enclave; attestation flaws are a stated risk.
5. **Keep data local**: federated learning trains across devices or organisations without centralising data.
6. **Reduce exposure**: synthetic data, pseudonymisation, obfuscation and data minimisation.
7. **Main use cases**: test data management, financial transactions, healthcare and data transfers between parties.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[PET]] | The family of technologies |
| [[Security]] | Compliance and breach reduction |
| [[Secure Analytics - Federated Learning and Secure Aggregation]] | Paper on FL and secure aggregation |
| [[Technological Enablers for Privacy Preserving Data Sharing and Analysis]] | Related survey |

# When to use

1. When **choosing a PET** for a data-sharing or ML scenario.
2. When you need **one-line definitions** for a privacy discussion.
3. When linking privacy techniques to ML work such as [[LightSecAgg - A Lighweight and versatile design for secure aggregation in federated learning]].

# Caveats

- Vendor-research article; the intro says "top 10" but lists 11, and several benefit/challenge cells are empty.

---
[[PET]] [[Security]] [[Machine Learning]]
[[Secure Analytics - Federated Learning and Secure Aggregation]]
[[Technological Enablers for Privacy Preserving Data Sharing and Analysis]]
[[PUMA - secure inference of LLaMa 7B in five minutes]]
[[How to create a private ChatGPT that interacts with your local documents]]
