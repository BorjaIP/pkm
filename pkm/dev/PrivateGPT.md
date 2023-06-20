---
title:  PrivateGPT
created: Tuesday 20th June 2023 18:38
aliases: 
tags: gpt
---

With [PrivateGPT](https://github.com/imartinez/privateGPT) can asks questions to your documents without an internet connection, using the power of LLMs.

- [GPT4All](https://github.com/nomic-ai/gpt4all)
- [GPT4AllChat](https://github.com/nomic-ai/gpt4all/tree/main/gpt4all-chat)
- [LangChain](https://python.langchain.com/en/latest/modules/models/llms/integrations/gpt4all.html)
- [PrivateGPT-local-llm](https://bdtechtalks.com/2023/06/01/create-privategpt-local-llm/)

conda create gpt4all
conda activate gpt4all
conda install python=3.10

https://github.com/nomic-ai/gpt4all/issues/876
https://github.com/nomic-ai/gpt4all/tree/main/gpt4all-bindings/python#local-build-instructions

git clone --recurse-submodules https://github.com/nomic-ai/gpt4all
git checkout tags/v1.4.0
CC=/usr/local/bin/gcc CXX=/usr/local/bin/g++ cmake -DCMAKE_CXX_COMPILER='g++' -DCMAKE_C_COMPILER='gcc' ..
CC=/usr/local/bin/gcc CXX=/usr/local/bin/g++ cmake -DCMAKE_CXX_COMPILER='g++' -DCMAKE_C_COMPILER='gcc' --build . --parallel

cd ../../gpt4all-bindings/python
pip3 install -e .

- update langchain==0.0.190 in requirements.txt

CC=/usr/local/bin/gcc CXX=/usr/local/bin/g++ pip install -r requirements.txt

- Chat

https://github.com/kuvaus/LlamaGPTJ-chat

git clone --recurse-submodules https://github.com/kuvaus/LlamaGPTJ-chat
cd LlamaGPTJ-chat
git checkout tags/v0.2.4
mkdir build
cd build
CC=/usr/local/bin/gcc CXX=/usr/local/bin/g++ cmake -DCMAKE_CXX_COMPILER='g++' -DCMAKE_C_COMPILER='gcc' ..
CC=/usr/local/bin/gcc CXX=/usr/local/bin/g++ cmake -DCMAKE_CXX_COMPILER='g++' -DCMAKE_C_COMPILER='gcc' --build . --parallel

cd build
./chat -m "/workspace/privateGPT/models/ggml-gpt4all-j-v1.3-groovy.bin" -t 4
