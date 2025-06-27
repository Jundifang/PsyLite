# PsyLite: A lightweight mental-support AI agent based on ​InternLM2.5-7B-Chat with appropriate crosstalks 
<div align="center">
  <img src="assets\logo.png" width="200"/>



</div>
<div align="center" style="line-height: 1;">
  
  
<a href="http://arxiv.org/abs/2506.21536"><img alt="arXiv"
    src="https://img.shields.io/badge/arXiv-Technical%20Report-b31b1b?logo=arxiv&logoColor=white"/></a>
<a href="https://ollama.com/Juneup/internlm2.5_7b_distill"><img alt="internlm2.5_7b_distill"
    src="https://img.shields.io/badge/%F0%9F%90%91internlm2.5_7b_distill-Ollama-ffc107?color=white&logoColor=white"/></a>
<a href="https://huggingface.co/juneup/internlm2.5_7b_distill_orpo"><img alt="internlm2.5_7b_distill_orpo"
    src="https://img.shields.io/badge/%F0%9F%A4%97%20internlm2.5_7b_distill_orpo-Hugging%20Face-ffc107?color=ffc107&logoColor=white"/></a>
   
  <br>
 
</div>

## 📖 Content
- [PsyLite](#psylite-a-lightweight-mental-support-ai-agent-based-on-internlm25-7b-chat-with-appropriate-crosstalks)
  - [📖 Content](#-content)
  - [🔄 Architecture Diagram](#-architecture)
  - [🎉 News](#-news)
  - [📝 Introduction](#-introduction)
    - [Basic feature](#basic-feature)
    - [Advanced feature](#advanced-feature)
    - [Model list](#model-list)
  - [🛠️ Deployment](#%EF%B8%8F-deployment)
  - [✨ Open Source List](#-open-source-list)
    - [1. internlm2.5_7b_distill](#1-internlm25_7b_distill)
    - [2. internlm2.5_7b_distill_orpo](#2-internlm25_7b_distill_orpo)
    - [3. Config File Used for Training](#3-config-file-used-for-training)
    - [4. Pipelines for PsyLite](#4-pipelines-for-psylite)
    - [5. Crosstalk Examples](#5-crosstalk-examples)
  - [🎖️ Acknowledgements](#%EF%B8%8F-acknowledgements)
  - [🌟 Star History](#-star-history)

## 🔄 Architecture
<div align="center">
  <img src="assets\structure.png" width="800"/>
  <h4 align="center">Overall Architecture Diagram</h4>
</div>




## 🎉 News

- **\[2025/05\]** Finish developing [**pipelines**](https://github.com/open-webui/pipelines) for [**PsyLite**](https://github.com/Jundifang/PsyLite/blob/main/pipelines/PsyLite.py) ! [What's new?](#Advanced-feature)
- **\[2025/04\]** Finish training model **internlm2.5_7b_distill** and **internlm2.5_7b_distill_orpo**  .

## 📝 Introduction
  
### Basic feature

A large model application for mild psychological counseling with low hardware requirements and deep thinking ability developed based on internlm2.5-7b-chat
<div align="center">
  <img src="assets\conversation.png" width="800"/>
  <h4 align="center">Conversation Example</h4>
</div>

### Advanced feature

**Condition RAG**: Determine whether it is suitable for the current user to use crosstalk 
> for the purpose of livening up the atmosphere, narrowing the mutual distance, etc.
- If it is **suitable**, RAG retrieves the crosstalk corpus and provides it to the model to generate an answer at the same time. 
- If it is **not suitable** and is **not a dangerous conversation**, skip RAG directly. 
- If it is **not suitable** and is a **dangerous conversation**, answer with preset phrases to prevent dangerous conversations and suggest the user seek for professional help.

<div align="center">
  <img src="assets\pipelines.png" width="600"/>
  <h4 align="center">Archetecture of Pipelines for PsyLite </h4>
</div>

This enables the retrieval of the corpus only in appropriate situations during psychological counseling to provide crosstalk segments to improve the user's experience.

<div align="center">
  <img src="assets\multi_type.png" width="800"/>
  <h4 align="center">Multi_type Conversation</h4>
</div>

### Model list
|Platform |     Model       |   
| :----------: | :----------: | 
|Hugging Face|   [internlm2.5_7b_distill](https://huggingface.co/juneup/internlm2.5_7b_distill)              |  
|Hugging Face|   [internlm2.5_7b_distill_orpo](https://huggingface.co/juneup/internlm2.5_7b_distill_orpo)         | 
|Ollama|   [internlm2.5_7b_distill_q4_k_m](https://ollama.com/Juneup/internlm2.5_7b_distill:q4_k_m)              | 
|Ollama|   [internlm2.5_7b_distill_orpo_q4_k_m](https://ollama.com/Juneup/internlm2.5_7b_distill:orpo_q4_k_m)              | 

**welcome Star⭐、PR and Issues**

## 🛠️ Deployment
1. **Install [Ollama](https://ollama.com/)**
2. **Install And Configure [Open-webui](https://github.com/open-webui/open-webui)**
3. **Install And Get [PIPELINES](https://github.com/open-webui/pipelines) Connected to open-webui**
4. **Import [PsyLite.py](https://github.com/Jundifang/PsyLite/blob/main/pipelines/PsyLite.py) to Pipelines And Configure its Valves Parameters、RAG File Path**
5. **Have fun !**

> [!TIP]
> **To get better performance, we reccommand to set system prompt**, [see here](https://github.com/Jundifang/PsyLite/blob/main/assets/prompt.txt)

## ✨ Open Source List
the base model of internlm2.5_7b_distill and internlm2.5_7b_distill_orpo is [internlm2_5-7b-chat](https://huggingface.co/internlm/internlm2_5-7b-chat) 。

### 1. internlm2.5_7b_distill

Architecture Diagram
<div align="center">
  <img src="assets\distill.png" width="450"/>
</div>

<details>
<summary> model download</summary>

```bash
git lfs install
git clone https://huggingface.co/juneup/internlm2.5_7b_distill
```
If you want to clone without large files - just their pointers：
```bash
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/juneup/internlm2.5_7b_distill
```
Ollama
```bash
ollama run Juneup/internlm2.5_7b_distill:q4_k_m
```

</details>

### 1.1 Datasets Used for Training:
 [**juneup/psy-mix-gen-distill-13k**](https://huggingface.co/datasets/juneup/psy-mix-gen-distill-13k)

### 2. internlm2.5_7b_distill_orpo
Architecture Diagram
<div align="center">
  <img src="assets\distill_orpo.png" width="800"/>
</div>

<details>
<summary> model download</summary>

```bash
git lfs install
git clone https://huggingface.co/juneup/internlm2.5_7b_distill_orpo
```
If you want to clone without large files - just their pointers：
```bash
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/juneup/internlm2.5_7b_distill_orpo
```
Ollama
```bash
ollama run Juneup/internlm2.5_7b_distill:orpo_q4_k_m
```

</details>


### 2.1 Datasets Used for Training:
 [**juneup/PKU-SafeRLHF-orpo-72k**](https://huggingface.co/datasets/juneup/PKU-SafeRLHF-orpo-72k)


### 3. Config File Used for Training

[Click to see details](https://github.com/Jundifang/PsyLite/blob/main/config)


### 4. Pipelines for PsyLite

> [!TIP]
> **INSTALL [PIPELINES](https://github.com/open-webui/pipelines) BEFORE USING PsyLite!**

[Click to jump to **PsyLite.py**](https://github.com/Jundifang/PsyLite/blob/main/pipelines/PsyLite.py)

### 5. Crosstalk Examples

[Click to see details](https://github.com/Jundifang/PsyLite/blob/main/data)


## 🎖️ Acknowledgements

| Team | Description |
|---|---|
| [Shanghai Artificial Intelligence Laboratory](https://www.shlab.org.cn/) | Thanks for the technical and platform support |
| [Xtuner](https://github.com/InternLM/xtuner) | Thanks for the training toolkits |
| [OpenCompass](https://github.com/open-compass/opencompass) | Thanks for the evaluation toolkits |
| [llama.cpp](https://github.com/open-compass/opencompass) | Thanks for the model weight file converter |
| [Open-webui](https://github.com/open-webui/open-webui) | Thanks for the excellent deployment platform | 
| [Pieplines](https://github.com/open-webui/pipelines) | Thanks for pipelines for custom workflow|

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Jundifang/PsyLite&type=Date)](https://www.star-history.com/#Jundifang/PsyLite&Date)