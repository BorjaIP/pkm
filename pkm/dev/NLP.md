---
title: NLP
created: Monday 5th February 2024 12:23
aliases: 
tags:
  - ai
---
**Natural language processing** (NLP) is a form of artificial intelligence that allows computers to understand human language, whether it be written, spoken, or even scribbled.

![[nlp.png]]
## Natural language techniques 

NLP encompasses a wide range of techniques to analyze human language. Some of the most common techniques you will likely encounter in the field include:

- **Sentiment analysis:** An NLP technique that analyzes text to identify its sentiments, such as “positive,” “negative,” or “neutral.” Sentiment analysis is commonly used by businesses to better understand customer feedback. 
- **Summarization:** An NLP technique that summarizes a longer text, in order to make it more manageable for time-sensitive readers. Some common texts that are summarized include reports and articles.
- **Keyword extraction:** An NLP technique that analyzes a text to identify the most important keywords or phrases. Keyword extraction is commonly used for [search engine optimization (SEO)](https://www.coursera.org/articles/seo-marketing), social media monitoring, and business intelligence purposes. 
- **Tokenization:** The process of breaking characters, words, or subwords down into “tokens” that can be analyzed by a program. Tokenization undergirds common NLP tasks like word modeling, vocabulary building, and frequent word occurrence.
## Models

### Latent Dirichlet Allocation (LDA)

**Latent Dirichlet Allocation** (LDA) is a popular form of statistical topic modeling. In LDA, documents are represented as a mixture of topics and a topic is a bunch of words. Those topics reside within a hidden, also known as a latent layer. 

LDA looks at a document to determine a set of topics that are likely to have generated that collection of words. So, if a document uses certain words that are contained in a topic, you could say the document is about that topic.

### Latent Semantic Analysis (LSA)

**Latent Semantic Analysis** is a natural language processing method that analyzes relationships between a set of documents and the terms contained within. It uses singular value decomposition, a mathematical technique, to scan unstructured data to find hidden relationships between terms and concepts.

LSA is primarily used for concept searching and automated document categorization. However, it’s also found use in software engineering (to understand source code), publishing (text summarization), search engine optimization, and other applications.

There are a number of drawbacks to Latent Semantic Analysis, the major one being is its inability to capture polysemy (multiple meanings of a word). The vector representation, in this case, ends as an average of all the word’s meanings in the corpus. That makes it challenging to compare documents.

### Term Frequency-Inverse Document Frequency (TF-IDF)

**TF-IDF (term frequency-inverse document frequency)** is a statistical measure that evaluates how relevant a word is to a document in a collection of documents.

This is done by multiplying two metrics: how many times a word appears in a document, and the inverse document frequency of the word across a set of documents.

TF-IDF was invented for document search and information retrieval. It works by increasing proportionally to the number of times a word appears in a document, but is offset by the number of documents that contain the word. So, words that are common in every document, such as this, what, and if, rank low even though they may appear many times, since they don’t mean much to that document in particular.