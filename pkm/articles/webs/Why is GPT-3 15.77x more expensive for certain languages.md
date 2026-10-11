---
title:  Why is GPT-3 15.77x more expensive for certain languages
created: Monday 14th April 2025 20:49
aliases: 
tags:
  - llm
  - gpt
  - nlp
  - tokenization
---
- https://denyslinkov.medium.com/why-is-gpt-3-15-77x-more-expensive-for-certain-languages-2b19a4adc4bc
- Type: article
- Source: Medium · Denys Linkov · Jan 2023

---

# TL;DR

English-optimised **tokenizers** make the same sentence use up to 15.77x more tokens in other languages, which raises cost, latency and limits for non-English users of [[GPT]] models.

# Summary

LLM APIs bill per **token**, and tokenizers learn their units from mostly English text. Running the 1M-utterance **MASSIVE** dataset, translated into 51 languages, through eight tokenizers shows GPT and OPT with the widest spread between languages, while models such as NLLB are balanced. At GPT-3 DaVinci pricing, the most tokenised language cost $27.98 against $1.76 for the cheapest. A prompt-plus-response test gave a similar 15.69x gap between English and Malayalam.

# Key takeaways

1. **Tokens, not words, set the price**: the same utterance can need several times more tokens depending on language and tokenizer.
2. **Measure with a shared dataset**: MASSIVE gives parallel utterances across 51 languages to compare tokenizers fairly.
3. **Expect four side effects** beyond cost: slower responses (one token generated at a time), shorter usable prompts, more limited outputs, and weaker accuracy for small-corpus languages.
4. **Choose tokenizers deliberately**: 5 of the 8 tested had narrow spreads; the multilingual NLLB model had the best ratio.
5. **Consider the equity angle**: USD-priced APIs are costlier relative to local income, and English-prompted competitors can undercut local-language startups.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[GPT]] | GPT-3 tokenizer and pricing used as the example |
| [[LLM]] | Models whose cost depends on tokenization |
| [[NLP]] | Tokenization as a core preprocessing step |
| [[Transformers]] | Architecture generating one token at a time |
| MASSIVE, NLLB | Multilingual dataset and open translation model for 200 languages |

# When to use

1. When **estimating LLM cost** for non-English content.
2. When explaining **why tokenization matters** beyond preprocessing.
3. When choosing a **multilingual model or tokenizer** for a product.

# Caveats

- 2023 snapshot: GPT-3 prices, the 2048-token prompt limit and tokenizers have since changed; the mechanism, not the figures, is the lasting insight.
- Cost figures come from the author's own experiment, run on a sample of utterances.

---
[[LLM]] [[GPT]] [[NLP]] [[Transformers]]
[[A Survey of Large Language Models]]
