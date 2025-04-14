---
title:  ColossalAI
created: Tuesday 20th June 2023 20:06
aliases: 
tags: gpt, llm 
---
[Colossal-AI](https://github.com/hpcaitech/ColossalAI) provides a collection of parallel components for you. We aim to support you to write your distributed deep learning models just like how you write your model on your laptop. We provide user-friendly tools to kickstart distributed training and inference in a few lines.

Making large AI models cheaper, faster and more accessible.

- [[ColossalAI-Chat]]
- [[ColossalChat - An Open-Source Solution for Cloning ChatGPT With a Complete RLHF Pipeline]]
- [[Large Scale Distributed Model Training with Colossal AI and Lightning AI]]
- [[Replicate ChatGPT Training Quickly and Affordable with Open Source Colossal-A]]
## MiniChatGPT

- [MiniChatGPT](https://github.com/juncongmoo/minichatgpt) | To Train ChatGPT In 5 Minutes with ColossalAI
# Installation and configuration

**WARNING**: Install torch 1.12.1

```bash
git checkout tags/v0.2.8
conda activate coati
```

- Download transformer.

```bash
git clone https://github.com/hpcaitech/transformers
cd transformers
pip install .
```

- Reinstall colossalai

```bash
CUDA_HOME=$CONDA_PREFIX CUDA_EXT=1 pip install .

cd ColossalAI
pip install .
```

- Reinstall Coati

```bash
cd applications/Chat
pip install .
```

- Create a symbolic link for automate refresh.

```bash
ln -s /workspace/ColossalAI/colossalai/ colossalai
ln -s /workspace/ColossalAI/applications/Chat/coati coati
```

- Data for training models.

	- [InstructWild Data](https://github.com/XueFuzhao/InstructionWild/tree/main/data)
	- [instinwild_en.json](https://drive.google.com/file/d/1qOfrl0RIWgH2_b1rYCEVxjHF3u3Dwqay/view

```bash
cd /ColossalAI/applications/Chat/examples
```

- Multiple nodes

```bash
WORLD_SIZE=6  CUDA_VISIBLE_DEVICES=0,1,2,3,4,5 torchrun \
    --nnodes 3 \
    --nproc_per_node 6 \
    --master_addr="${MASTER_ADDR}" \
    --master_port="${MASTER_PORT}" \
    --node_rank ${NODE_RANK} \
    train_prompts.py \
    --pretrain "llama_7b_hf/" \
    --model 'llama' \
    --strategy colossalai_gemini \
    --prompt_dataset ColossalAI/Belle_open_source_0.5M.json \
    --rm_model 'llama' \
    --rm_pretrain "/llama_7b_hf/" \
    --lora_rank 2
```
## Stage 1

- BloomForCausalLM

```bash
export OMP_NUM_THREADS=8

python train_sft.py --pretrain 'bigscience/bloom-560m' \
                    --model 'bloom' \
                    --strategy naive \
                    --log_interval 10 \
                    --save_path '/workspace/ColossalAI/applications/Chat/output_model/stage_1' \
                    --dataset 'data/instinwild_en.json' \
                    --batch_size 1 \
                    --accimulation_steps 8 \
                    --lr 2e-5 \
                    --max_datasets_size 512 \
                    --max_epochs 1 \
                    --lora_rank 16

nohup ./train_sft.sh &
```
## Stage 2

- BloomModel

```bash
export OMP_NUM_THREADS=8

python train_reward_model.py --pretrain '/workspace/ColossalAI/applications/Chat/output_model/stage_1' \
                             --model 'bloom' \
                             --strategy naive \
                             --loss_fn 'log_exp'\
                             --lora_rank 16 \
                             --save_path '/workspace/ColossalAI/applications/Chat/output_model/stage_2/rmstatic.pt' \
                             --test True

nohup ./train_rm.sh &
```
## Stage 3

- Generate dataset prompt

```bash
python generate_prompt_dataset.py --dataset_path data/instinwild_en.json --save_path ./data/prompt_samples_100.csv --sample_size 100

export OMP_NUM_THREADS=8

python train_prompts.py --pretrain '/workspace/ColossalAI/applications/Chat/output_model/stage_1' \
                        --prompt_dataset data/prompt_samples_100.csv \
                        --pretrain_dataset data/instinwild_en.json \
                        --model 'bloom' \
                        --strategy naive \
                        --rm_path '/workspace/ColossalAI/applications/Chat/output_model/stage_2/rmstatic.pt'\
                        --save_path '/workspace/ColossalAI/applications/Chat/output_model/stage_3/rf_model.pt' \
                        --lora_rank 16 \
                        --train_batch_size 1 \
                        --max_epochs 1

```
## Script

```python
import torch
state_dict = torch.load('/workspace/ColossalAI/applications/Chat/output_model/stage_2/rmstatic.pt', map_location=torch.device('cpu'))

state_dict = torch.load('/workspace/ColossalAI/applications/Chat/output_model/stage_1.pt', map_location=torch.device('cpu'))

for key in list(state_dict.keys()):
    if 'model.' in key:
        state_dict[key.replace('model.', '')] = state_dict[key]
        del state_dict[key]

for key in list(state_dict.keys()):
    state_dict['model.' + key] = state_dict[key]
    del state_dict[key]

from transformers import BloomConfig, BloomForCausalLM, BloomModel
from coati.models.bloom import BLOOMRM, BLOOMActor, BLOOMCritic

rm_model = BloomModel(BloomConfig())
rm_model = BloomModel.from_pretrained('bigscience/bloom-560m')
rm_model.load_state_dict(state_dict, strict=False)

checkpoint = "/workspace/ColossalAI/applications/Chat/output_model/stage_2/rmstatic.pt"
config = BloomConfig.from_pretrained(checkpoint)

BloomForCausalLM.from_pretrained('/workspace/ColossalAI/applications/Chat/output_model/stage_1')

a = BLOOMActor(pretrained='bigscience/bloom-560m', lora_rank=16)
a.load_state_dict(state_dict, strict=False)
a = BLOOMActor(pretrained='/workspace/ColossalAI/applications/Chat/output_model/stage_1')

rm = BLOOMRM(pretrained='bigscience/bloom-560m', lora_rank=16)
rm.load_state_dict(state_dict, strict=False)

c = BLOOMCritic(pretrained='bigscience/bloom-560m', lora_rank=16)
c.load_state_dict(state_dict, strict=False)

with init_empty_weights():
    model = AutoModelForCausalLM.from_config(config)

from coati.models import convert_to_lora_module
model = BloomForCausalLM.from_pretrained('bigscience/bloom-560m')
l = convert_to_lora_module(model, 16)
l.load_state_dict(state_dict)

load_in_8bit=True,
torch_dtype=torch.float16,
device_map="auto",

rm_model - type model
rm_path - BLOOMRM
rm_pretrain - BLOOMCritic

mlm = BloomForCausalLM(BloomConfig())
mlm.load_state_dict(model)

for key, value in model.items():
    key = key[4:] # remove `att.`
    new_state_dict[key] = value

BloomModel.from_pretrained(state_dict='/workspace/ColossalAI/applications/Chat/output_model/stage_2/rmstatic.pt', from_tf=True)
```


