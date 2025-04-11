---
title:  PrivateGPT
created: Tuesday 20th June 2023 18:38
aliases: 
tags: gpt
---
[PrivateGPT](https://github.com/imartinez/privateGPT) is a production-ready AI project that allows you to ask questions about your documents using the power of Large Language Models ([[LLM]]), even in scenarios without an Internet connection. 100% private, no data leaves your execution environment at any point.
## Articles/Talks
- [How to create a private ChatGPT that interacts with your local documents](https://bdtechtalks.com/2023/06/01/create-privategpt-local-llm/)
- [GPT4All](https://github.com/nomic-ai/gpt4all)
- [GPT4AllChat](https://github.com/nomic-ai/gpt4all/tree/main/gpt4all-chat)
- [LangChain](https://python.langchain.com/en/latest/modules/models/llms/integrations/gpt4all.html)
- [PrivateGPT-local-llm](https://bdtechtalks.com/2023/06/01/create-privategpt-local-llm/)


<iframe width="560" height="315" src="https://www.youtube.com/embed/A3F5riM5BNE?si=xt1wFhYsJ9Gg5Qkt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```bash
conda create gpt4all
conda activate gpt4all
conda install python=3.10
```

- Build [GPT4All](https://github.com/nomic-ai/gpt4all) from source

https://github.com/nomic-ai/gpt4all/issues/876
https://github.com/nomic-ai/gpt4all/tree/main/gpt4all-bindings/python#local-build-instructions

```bash
git clone --recurse-submodules https://github.com/nomic-ai/gpt4all
CC=/usr/local/bin/gcc CXX=/usr/local/bin/g++ cmake -DCMAKE_CXX_COMPILER='g++' -DCMAKE_C_COMPILER='gcc' ..
CC=/usr/local/bin/gcc CXX=/usr/local/bin/g++ cmake -DCMAKE_CXX_COMPILER='g++' -DCMAKE_C_COMPILER='gcc' --build . --parallel
cd ../../gpt4all-bindings/python
pip3 install -e .
```

- Update `langchain==0.0.190` in requirements.txt

```bash
CC=/usr/local/bin/gcc CXX=/usr/local/bin/g++ pip install -r requirements.txt
```

- Chat

- [LlamaGPTJ-chat](https://github.com/kuvaus/LlamaGPTJ-chat)

```bash
git clone --recurse-submodules https://github.com/kuvaus/LlamaGPTJ-chat
cd LlamaGPTJ-chat
git checkout tags/v0.2.4
mkdir build
cd build
CC=/usr/local/bin/gcc CXX=/usr/local/bin/g++ cmake -DCMAKE_CXX_COMPILER='g++' -DCMAKE_C_COMPILER='gcc' ..
CC=/usr/local/bin/gcc CXX=/usr/local/bin/g++ cmake -DCMAKE_CXX_COMPILER='g++' -DCMAKE_C_COMPILER='gcc' --build . --parallel
cd build
./chat -m "privateGPT/models/ggml-gpt4all-j-v1.3-groovy.bin" -t 4
```

## RAG

- [IncarnaMind](https://github.com/junruxiong/IncarnaMind) - Connect and chat with your multiple documents (pdf and txt) through GPT, Claude and Local Open-Source LLMs