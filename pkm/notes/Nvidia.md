---
title: Nvidia
created: Thursday 20th July 2023 12:34
aliases: 
tags:
  - gpu
---

| Tool/Framework                                         | Description                                                                                           |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | Python API to define Large Language Models (LLMs) and build TensorRT engines                          |
| [nvtop](https://github.com/Syllo/nvtop)                | GPU & Accelerator process monitoring for AMD, Apple, Huawei, Intel, NVIDIA                            |
| [nvitop](https://github.com/XuehaiPan/nvitop)          | An interactive NVIDIA-GPU process viewer and beyond, the one-stop solution for GPU process management |

- [DeepFaceLab](https://github.com/iperov/DeepFaceLab)
- [DeepFaceLive](https://github.com/iperov/DeepFaceLive)
# NCCL

The NVIDIA Collective Communications Library (NCCL, pronounced “Nickel”) is **a library providing inter-GPU communication primitives that are topology-aware and can be easily integrated into applications**.

- See if NCLL is installed correctly.

```bash
find /usr -name "libnccl.so*" 2>/dev/null
```