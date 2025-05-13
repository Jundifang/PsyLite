# PsyLite - 心绎四相
<div align="center">
  <img src="assets\logo.png" width="300"/>

  <h3 align="center">PsyLite</h3>
  <br /><br />
</div>
<div align="center" style="line-height: 1;">
  
  <a href="https://huggingface.co/juneup/internlm2.5_7b_distill_orpo"><img alt="internlm2.5_7b_distill_orpo"
    src="https://img.shields.io/badge/%F0%9F%A4%97%20internlm2.5_7b_distill_orpo-Hugging%20Face-ffc107?color=ffc107&logoColor=white"/></a>
 
   <a href="https://ollama.com/Juneup/internlm2.5_7b_distill"><img alt="internlm2.5_7b_distill"
    src="https://img.shields.io/badge/%F0%9F%90%91internlm2.5_7b_distill-Ollama-ffc107?color=white&logoColor=white"/></a>
  <br>
 
</div>

## 📖 目录
- [PsyLite - 心绎四相](#psylite---心绎四相)
  - [📖 目录](#-目录)
  - [🔄 架构图](#-架构图)
  - [🎉 更新](#-更新)
  - [📝 简介](#-简介)
  - [🛠️ 部署](#️-部署)
    - [internlm2.5_7b_distill](#internlm25_7b_distill)
    - [internlm2.5_7b_distill_orpo](#internlm25_7b_distill_orpo)
  - [🎖️ 致谢](#️-致谢)

## 🔄 架构图
<div align="center">
  <img src="assets\PsyCrossFlow.jpg" width="800"/>
</div>

## 🎉 更新


## 📝 简介
使用 InternLM2.5-7B-Chat 作为基础模型，结合从 DeepSeek R1 提炼的数据以及心理咨询相关的数据，训练一个具备情绪分析和推理能力的心理咨询模型。
<div align="center">
  <img src="assets\conversation.png" width="800"/>
  <h3 align="center">Conversation</h3>
</div>

同时，我们尝试让模型学习对话相声四个步骤（垫话、瓢把儿、正活、攒底）来进行咨询，并根据用户的对话动态地切换角色（例如，当用户是故事讲述者时，模型的任务是帮助他探索；如果用户期望模型给出一些建议，那么模型就是故事讲述者）。
<div align="center">
  <img src="assets\crosstalk.png" width="800"/>
  <h3 align="center">Crosstalk</h3>
</div>

采用的模型列表如下：
|平台|     模型       |   
| :----------: | :----------: | 
|Hugging Face|   internlm2.5_7b_distill              |  
|Hugging Face|   internlm2.5_7b_distill_orpo         | 
|Hugging Face|   internlm2.5_7b_distill-Q4_K_M-GGUF  |  
|Hugging Face|   internlm2.5_7b_distill_orpo-Q4_K_M-GGUF     |  
|Ollama|   internlm2.5_7b_distill              | 


项目持续开发中，欢迎  Star⭐、PR 和 Issue。

## 🛠️ 部署
internlm2.5_7b_distill与internlm2.5_7b_distill_orpo的基座模型都采用internlm2.5-7b-chat(https://huggingface.co/juneup/internlm2.5_7b_distill) 。

接下来介绍二者模型与数据集及其下载方式。

### internlm2.5_7b_distill

架构图
<div align="center">
  <img src="assets\distill.png" width="800"/>
</div>

模型下载
```bash
git lfs install
git clone https://huggingface.co/juneup/internlm2.5_7b_distill
```
若不想克隆大型文件：
```bash
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/juneup/internlm2.5_7b_distill
```
在Ollama下载
```bash
ollama run Juneup/internlm2.5_7b_distill:q4_k_m
```
数据集组成

5k条精选通用领域含思维链数据(https://huggingface.co/datasets/Congliu/Chinese-DeepSeek-R1-Distill-data-110k-SFT)  +3k条含思维链心理辅导对话(https://huggingface.co/datasets/CAS-SIAT-XinHai/CPsyCoun) 。

数据集下载

通用领域含思维链数据集：
```bash
git lfs install
git clone https://huggingface.co/datasets/Congliu/Chinese-DeepSeek-R1-Distill-data-110k-SFT
```
若不想克隆大型文件：
```bash
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/Congliu/Chinese-DeepSeek-R1-Distill-data-110k-SFT
```
含思维链心理辅导对话数据集：
```bash
git lfs install
git clone https://huggingface.co/datasets/CAS-SIAT-XinHai/CPsyCoun
```
若不想克隆大型文件：
```bash
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/CAS-SIAT-XinHai/CPsyCoun
```

### internlm2.5_7b_distill_orpo
架构图
<div align="center">
  <img src="assets\distill_orpo.png" width="800"/>
</div>

模型下载
```bash
git lfs install
git clone https://huggingface.co/juneup/internlm2.5_7b_distill_orpo
```
若不想克隆大型文件
```bash
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/juneup/internlm2.5_7b_distill_orpo
```

在Ollama下载
```bash
ollama run Juneup/internlm2.5_7b_distill:orpo_q4_k_m
```
数据集组成

PKU-SafeRLHF(https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF-single-dimension) 经处理后最终数据集为(https://huggingface.co/datasets/juneup/PKU-SafeRLHF-orpo) 。

数据集下载

```bash
git lfs install
git clone https://huggingface.co/datasets/juneup/PKU-SafeRLHF-orpo
```
若不想克隆大型文件：
```bash
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/juneup/PKU-SafeRLHF-orpo
```

## 🎖️ 致谢
上海人工智能实验室(https://www.shlab.org.cn/) 提供技术与平台支持。



