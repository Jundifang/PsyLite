# PsyLite: A lightweight mental-support AI agent based on ​InternLM2.5-7B-Chat with appropriate crosstalks 
<div align="center">
  <img src="assets\logo.png" width="200"/>



</div>
<div align="center" style="line-height: 1;">
  
  <a href="https://huggingface.co/juneup/internlm2.5_7b_distill_orpo"><img alt="internlm2.5_7b_distill_orpo"
    src="https://img.shields.io/badge/%F0%9F%A4%97%20internlm2.5_7b_distill_orpo-Hugging%20Face-ffc107?color=ffc107&logoColor=white"/></a>
   <a href="https://ollama.com/Juneup/internlm2.5_7b_distill"><img alt="internlm2.5_7b_distill"
    src="https://img.shields.io/badge/%F0%9F%90%91internlm2.5_7b_distill-Ollama-ffc107?color=white&logoColor=white"/></a>
  <br>
 
</div>

## 📖 content
- [PsyLite](#psylite)
  - [📖 Content](#--content)
  - [🔄 Architecture Diagram](#-Architecture)
  - [🎉 News](#-news)
  - [📝 Introduction](#-introduction)
  - [🛠️ Deployment](#-deployment)
    - [internlm2.5_7b_distill](#internlm25_7b_distill)
    - [internlm2.5_7b_distill_orpo](#internlm25_7b_distill_orpo)
  - [🎖️ Acknowledgements](#-acknowledgements)

## 🔄 Architecture
<div align="center">
  <img src="assets\structure.png" width="800"/>
</div>

## 🎉 news

TODO

## 📝 introduction
A large model application for mild psychological counseling with low hardware requirements and deep thinking ability developed based on internlm2.5-7b-chat
<div align="center">
  <img src="assets\conversation.png" width="800"/>
  <h3 align="center">Conversation</h3>
</div>

**Advanced feature(development in progress)**

Condition RAG: Determine whether it is suitable for the current user to use crosstalk (for the purpose of livening up the atmosphere, narrowing the mutual distance, etc.). If it is suitable, RAG retrieves the crosstalk corpus and provides it to the model to generate an answer at the same time. If it is not suitable, skip RAG directly. This enables the retrieval of the corpus only in appropriate situations during psychological counseling to provide crosstalk segments to liven up the atmosphere.

<div align="center">
  <img src="assets\crosstalk.png" width="800"/>
  <h3 align="center">Crosstalk(TODO)</h3>
</div>

Model list：
|Platform |     Model       |   
| :----------: | :----------: | 
|Hugging Face|   [internlm2.5_7b_distill](https://huggingface.co/juneup/internlm2.5_7b_distill)              |  
|Hugging Face|   [internlm2.5_7b_distill_orpo](https://huggingface.co/juneup/internlm2.5_7b_distill_orpo)         | 
|Ollama|   [internlm2.5_7b_distill_q4_k_m](https://ollama.com/Juneup/internlm2.5_7b_distill:q4_k_m)              | 
|Ollama|   [internlm2.5_7b_distill_orpo_q4_k_m](https://ollama.com/Juneup/internlm2.5_7b_distill:orpo_q4_k_m)              | 

welcome  Star⭐、PR and Issues。

## 🛠️ deployment
the base model of internlm2.5_7b_distill and internlm2.5_7b_distill_orpo is [internlm2.5-7b-chat](https://huggingface.co/juneup/internlm2.5_7b_distill) 。

the following statements are models and datasets for PsyLite.

### internlm2.5_7b_distill

Architecture Diagram
<div align="center">
  <img src="assets\distill.png" width="800"/>
</div>

<details>
<summary> model download</summary>

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

</details>

### datasets used for training:
 [**juneup/psy-mix-gen-distill-13k**](https://huggingface.co/datasets/juneup/psy-mix-gen-distill-13k)

### internlm2.5_7b_distill_orpo
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
若不想克隆大型文件：
```bash
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/juneup/internlm2.5_7b_distill_orpo
```
在Ollama下载
```bash
ollama run Juneup/internlm2.5_7b_distill:orpo_q4_k_m
```

</details>


### datasets used for training:
 [**juneup/PKU-SafeRLHF-orpo-72k**](https://huggingface.co/datasets/juneup/PKU-SafeRLHF-orpo-72k)



## 🎖️ acknowledgements

| Organization | Description |
|---|---|
| [Shanghai Artificial Intelligence Laboratory](https://www.shlab.org.cn/) | Thanks for the technical and platform support |

## 🌟Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Jundifang/PsyLite&type=Date)](https://www.star-history.com/#Jundifang/PsyLite&Date)



