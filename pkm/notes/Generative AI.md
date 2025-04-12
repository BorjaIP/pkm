---
title: Generative AI
created: Monday 5th February 2024 13:20
aliases:
  - GenAI
tags:
---
**Generative AI** is a type of [[Artificial Intelligence]] that can produce content such as audio, text, code, video, images, and other data. Whereas traditional AI algorithms may be used to identify patterns within a training data set and make predictions, generative AI uses [[Machine Learning]] algorithms to create outputs based on a training data set. 
# Foundation Models

**Foundation model** is a term [popularized](https://arxiv.org/abs/2108.07258) by an institute at Stanford University. It refers to AI systems with broad capabilities that can be adapted to a range of different, more specific purposes. In other words, the original model provides a base (hence “foundation”) on which other things can be built. This is in contrast to many other AI systems, which are specifically trained and then used for a particular purpose.

Characteristics:

- Trained on massive and diverse datasets (internet-scale).
- Can be adapted (fine-tuned) to a wide range of downstream tasks.
- Handle multiple modalities (e.g., text, image, code).
# Text Generation

Generating human-like, contextually coherent text.
### Large Language Models ([[LLM]])

- Predict the next word/token in a sequence.
- Examples: GPT-3/4, LLaMA, Mistral, T5.

Applications:

- Content creation (articles, summaries)
- Conversational agents (chatbots)
- Code generation (e.g., GitHub Copilot)
- Text-based games, interactive fiction
## BERT

Released in 2018, **Bidirectional Encoder Representations from Transformers** ([BERT](https://huggingface.co/docs/transformers/model_doc/bert)) was one of the first foundation models. BERT is a bidirectional model that analyzes the context of a complete sequence then makes a prediction. It was trained on a plain text corpus and Wikipedia using 3.3 billion tokens (words) and 340 million parameters. BERT can answer questions, predict sentences, and translate texts.
## RoBERTa

[RoBERTa](https://huggingface.co/docs/transformers/model_doc/roberta) the full form for this is the Robustly Optimized BERT Pretraining Approach. In the series of attempts to improve the performance of the transformer architecture, RoBERTa is an enhanced version of the BERT model.
## [[GPT]]

The **Generative Pre-trained Transformer** (GPT) model was developed by OpenAI in 2018. It uses a 12-layer transformer decoder with a self-attention mechanism. And it was trained on the BookCorpus dataset, which holds over 11,000 free novels. A notable feature of GPT-1 is the ability to do zero-shot learning.
## BLOOM

[BLOOM](https://huggingface.co/bigscience/bloom) is a multilingual model with similar architecture to GPT-3. It was developed in 2022 as a collaborative effort involving over a thousand scientists and the Hugging Space team. **BLOOM** can create text in 46 languages and write code in 13 programming languages.

# Image & Video Generation

Create or manipulate visual content from text prompts or learned patterns.
## Diffusion Models

- Generate images by reversing a noise process (e.g., **Stable Diffusion**, **DALL·E 2**).
- Highly controllable and capable of high-quality outputs.
## Text-to-Image Models

- Input: natural language prompt → Output: image.
- Examples: Midjourney, DALL·E, Imagen (Google).
## Text-to-Video

- Still in development; generates video clips from descriptions.
- Examples: Runway ML, Sora (OpenAI), Meta Make-A-Video.
# Audio & Music Generatio

Produce natural-sounding speech, effects, or music compositions.

## Text-to-Speech (TTS)

- Convert text to spoken audio.
- Examples: Tacotron, WaveNet, ElevenLabs, Play.ht

## Music Generation

- AI that composes music in specific styles or instruments.
- Tools: AIVA, Amper Music, Google MusicLM.
## Voice Cloning

- Clone specific voices using short samples.
- Use cases: dubbing, virtual assistants, gaming.

# Multimodal Models

AI models that understand and generate across **multiple types of data** simultaneously.

## Input/Output Combinations

- Text + Image → Image (e.g., DALL·E)
- Image + Text → Caption (e.g., Flamingo, GPT-4V)
- Audio + Video → Text (e.g., Whisper)
# Evaluation

## Quantitative Metrics

- **BLEU, ROUGE** – for text overlap.
- **Fréchet Inception Distance (FID)** – for image realism.
- **WER/CER** – for speech-to-text accuracy.
## Qualitative Methods

- Human feedback and preference ranking.
- Alignment with task objectives (e.g., factuality, helpfulness).
## Safety and Bias Testing

- Analyze outputs for toxicity, bias, hallucinations, or disinformation.
# [[Prompt Engineering]]

# [[RAG]] (Retrieval-Augmented Generation)

# MCP ()
