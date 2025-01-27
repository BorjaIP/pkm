---
title:  Generative AI
created: Monday 5th February 2024 13:20
aliases: 
tags: 
---
**Generative AI** is a type of [[Artificial Intelligence]] that can produce content such as audio, text, code, video, images, and other data. Whereas traditional AI algorithms may be used to identify patterns within a training data set and make predictions, generative AI uses [[Machine Learning]] algorithms to create outputs based on a training data set. 

Generative AI can produce outputs in the same medium in which it is prompted (e.g., text-to-text) or in a different medium from the given prompt (e.g., text-to-image or image-to-video). Popular examples of generative AI include ChatGPT, Bard, DALL-E, Midjourney, and DeepMind.

**Foundation model** is a term [popularized](https://arxiv.org/abs/2108.07258) by an institute at Stanford University. It refers to AI systems with broad capabilities that can be adapted to a range of different, more specific purposes. In other words, the original model provides a base (hence “foundation”) on which other things can be built. This is in contrast to many other AI systems, which are specifically trained and then used for a particular purpose. Typical examples of foundation models include many of the same systems listed as [[LLM]]. 
# Models
## BERT

Released in 2018, **Bidirectional Encoder Representations from Transformers** ([BERT](https://huggingface.co/docs/transformers/model_doc/bert)) was one of the first foundation models. BERT is a bidirectional model that analyzes the context of a complete sequence then makes a prediction. It was trained on a plain text corpus and Wikipedia using 3.3 billion tokens (words) and 340 million parameters. BERT can answer questions, predict sentences, and translate texts.
## RoBERTa

[RoBERTa](https://huggingface.co/docs/transformers/model_doc/roberta) the full form for this is the Robustly Optimized BERT Pretraining Approach. In the series of attempts to improve the performance of the transformer architecture, RoBERTa is an enhanced version of the BERT model.
## GPT

The **Generative Pre-trained Transformer** ([[GPT]]) model was developed by OpenAI in 2018. It uses a 12-layer transformer decoder with a self-attention mechanism. And it was trained on the BookCorpus dataset, which holds over 11,000 free novels. A notable feature of GPT-1 is the ability to do zero-shot learning.
## BLOOM

[BLOOM](https://huggingface.co/bigscience/bloom) is a multilingual model with similar architecture to GPT-3. It was developed in 2022 as a collaborative effort involving over a thousand scientists and the Hugging Space team. **BLOOM** can create text in 46 languages and write code in 13 programming languages.

