"""
title: Conditional RAG Pipeline With Llama_Index And Ollama
author: Jun
author_url: https://github.com/Jundifang
date: 2025-05
version: 1.0
license: MIT
description: The pipeline of PsyLite for conditional retrieving relevant information from a knowledge base using the Llama Index library with Ollama embeddings.
requirements: llama-index, llama-index-llms-ollama, llama-index-embeddings-ollama
"""

from typing import List, Union, Generator, Iterator, Optional
from schemas import OpenAIChatMessage
import os
import re
from utils.pipelines.main import get_last_user_message, get_last_assistant_message,get_system_message
from openai import OpenAI 
import requests
from pydantic import BaseModel
import time
from pprint import pprint



class Pipeline:

    class Valves(BaseModel):
        LLAMAINDEX_OLLAMA_BASE_URL: str
        LLAMAINDEX_MODEL_NAME: str
        OLLAMA_MODEL_NAME: str
        LLAMAINDEX_EMBEDDING_MODEL_NAME: str
        JUDEGE_MODEL_NAME: str
        JUDGE_API_BASE_URL: str
        JUDGE_MODEL_API: str
        TAG_GEN_MODEL_NAME: str

    def __init__(self):
        self.documents = None
        self.index = None
        self.judge_result= None
        self.rag_result = None
        self.judge_code=None
        self.activate_model = None
        self.valves = self.Valves(
            **{
                "LLAMAINDEX_OLLAMA_BASE_URL": os.getenv("LLAMAINDEX_OLLAMA_BASE_URL", "http://host.docker.internal:11434"),
                "LLAMAINDEX_MODEL_NAME": os.getenv("LLAMAINDEX_MODEL_NAME", "qwen3:0.6b"),
                "LLAMAINDEX_EMBEDDING_MODEL_NAME": os.getenv("LLAMAINDEX_EMBEDDING_MODEL_NAME", "bge-m3:latest"),
                "JUDEGE_MODEL_NAME": os.getenv("JUDEGE_MODEL_NAME", "glm-4-flash-250414"),
                "JUDGE_API_BASE_URL": os.getenv("JUDGE_API_BASE_URL", ""),
                "JUDGE_MODEL_API": os.getenv("JUDGE_MODEL_API",""),
                "OLLAMA_MODEL_NAME": os.getenv("OLLAMA_MODEL_NAME", "qwen3:0.6b"),
                "TAG_GEN_MODEL_NAME":  os.getenv("TAG_GEN_MODEL_NAME", "qwen3:0.6b")
            }
        )

    async def inlet(self, body: dict, user: Optional[dict] = None) -> dict:
        # This function is called before the OpenAI API request is made. You can modify the form data before it is sent to the OpenAI API.
        
        print(f"inlet: {__name__} - body:")
        pprint(body)

        user_message = get_last_user_message(body["messages"])
        
        
        pprint(f"user_messages:{user_message}")
        messages=body["messages"][:-1]
        pprint(f"messages_list:{messages}")
        
        if "task" in body["metadata"]:
            print("titie / tag generated")
            self.activate_model=self.valves.TAG_GEN_MODEL_NAME
            self.judge_result = None
        else:
            print("user generated") 
            self.activate_model=self.valves.OLLAMA_MODEL_NAME
            self.judge_result = self.request(user_message,messages)
            
        print(2*"\n", "Raw judge_result:", self.judge_result, 2*"\n")

        return body
    
    async def outlet(self, body: dict, user: Optional[dict] = None) -> dict:
        print(f"outlet:{__name__}")
        messages = body["messages"]

        assistant_message = get_last_assistant_message(messages)
        print(f"Assistant message: {assistant_message}")
        
        if self.judge_code == "2":
            # 处理 self.rag_result：只保留从“甲：”开始的内容
            if self.rag_result:
                match = re.search(r'甲：', self.rag_result)
                if match:
                    rag_content = self.rag_result[match.start():]  # 从“甲：”开始截取
                else:
                    rag_content = self.rag_result  # 没找到“甲：”，保留原样
            else:
                rag_content = ""
                
            # 处理 self.rag_result：替换所有 \n\n 为 \n
            rag_content = rag_content.replace("\n\n", "\n") if rag_content else ""
            
            print(f"final rag_content: {rag_content}")
            
            for message in reversed(messages):
                if message["role"] == "assistant":
                    message["content"] = assistant_message+f"\n\n<details>\n<summary>很高兴看到你心情愉悦的样子，这一段相声送给你，希望你喜欢~</summary>\n```相声\n{rag_content}\n```\n\n</details>"
                    break

        return body
    
    
    
    
    def request(self,user_message: str,messages: List[dict]):

        print("执行状态评估ing")
        client = OpenAI(
            api_key=self.valves.JUDGE_MODEL_API,
            base_url=self.valves.JUDGE_API_BASE_URL
        ) 
        system_prompt = '''
        你是一个专业的心理健康评估师,你必须综合考量用户的回复以及历史聊天记录，给用户的当前状况进行打分
        
        输出要求：{0或1或2},{打分理由}
        打分说明：0代表用户当前情况非常危险，必须马上停止AI心理辅导，转由人工进行心理咨询、心理治疗。
        1代表用户当前情况正常，可以继续与AI进行对话
        2代表用户当前心情愉悦，可以在对话中增加幽默、调侃的语句,比如相声、脱口秀的方式来提升用户体验。
        '''
        
        message_content=f'''
        用户回复：{user_message}
        历史聊天记录：{messages}
        '''
        
        completion = client.chat.completions.create(
            model=self.valves.JUDEGE_MODEL_NAME,
            messages=[    
                {"role": "system", "content": system_prompt},    
                {"role": "user", "content": message_content},
            ],
            top_p=0.7,
            temperature=0
        ) 
        
        return completion.choices[0].message.content
        
    async def on_startup(self):
        from llama_index.embeddings.ollama import OllamaEmbedding
        from llama_index.llms.ollama import Ollama
        from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader

        Settings.embed_model = OllamaEmbedding(
            model_name=self.valves.LLAMAINDEX_EMBEDDING_MODEL_NAME,
            base_url=self.valves.LLAMAINDEX_OLLAMA_BASE_URL,
        )
        Settings.llm = Ollama(
            model=self.valves.LLAMAINDEX_MODEL_NAME,
            base_url=self.valves.LLAMAINDEX_OLLAMA_BASE_URL,
        )

        # This function is called when the server is started.
        global documents, index

        self.documents = SimpleDirectoryReader("/app/data").load_data()
        if self.documents is None:
            print( "No documents found")
        self.index = VectorStoreIndex.from_documents(self.documents)

        pass

    async def on_shutdown(self):
        # This function is called when the server is stopped.
        pass

    def pipe(
    self, user_message: str, model_id: str, messages: List[dict], body: dict
) -> Union[str, Generator, Iterator]:
    

        if self.index is None:
            return "No index found"

        # 解析 judge_result 中的序号部分
        if self.judge_result is not None:
            try:
                match = re.search(r'\d', self.judge_result)
                if match:
                    self.judge_code = match.group(0)
                else:
                    raise ValueError("No digit found in judge_result")
            except Exception as e:
                print(f"Failed to parse judge_result: {e}")
                self.judge_code = ""

            print("Parsed judge_code:", self.judge_code)

        # 0：非常危险，推荐人工介入
        if self.judge_code == "0":
            print("状态评估结果：0")
            return "很抱歉，我只是一个AI小助手，您的情况我力不从心，请您拨打全国各地免费心理热线12356，或者寻求专业心理咨询师的帮助，请您理解🌹"

        # 2：用户心情好，可以加入幽默元素
        else:
            if self.judge_code == "2":
                print("状态评估结果：2")

                system_prompt = get_system_message(messages)

                prompt = f'''{system_prompt}

                    同时你也是一个非常把握尺度分寸的相声大师，当前情况是：用户当前情况好，适合使用相声、脱口秀的方式来缓解氛围、拉进距离，你需要一步步深度思考一个相声小段子，你可以在知识库中检索适合当前语境的相声片段，或者自己写一段符合语境的、完整简单的对话相声段子
                    输出要求:
                    1. 相声段子5-10行即可
                    2. 使用相声段子讲求循序渐进，具有教育意义
                    3. 不允许添加任何描述性文字或说明，每段对话必须严格遵循以下格式：
                        甲：台词
                        乙：台词
                        

                    已知用户回复：{user_message}
                /no_think'''

                query_engine = self.index.as_query_engine()
                self.rag_result  = query_engine.query(prompt).response
                print(f"检索结果：{self.rag_result}")
                # body["messages"][-1]["content"] = f"你需要回应用户的问题，并在回复中的恰当位置原封不动地插入相声段子。\n\n用户回复：{user_message}"

            # 默认情况：1 或无法识别，正常流程
            else:
                print(f"未知或默认处理 (judge_code={self.judge_code})，继续常规对话")

            # 调用LLM生成最终回复
            try:
                print("生成最终结果")

                r = requests.post(
                    url=f"{self.valves.LLAMAINDEX_OLLAMA_BASE_URL}/v1/chat/completions",
                    json={**body, "model": self.activate_model},
                    stream=True,
                )

                r.raise_for_status()

                if body["stream"]:
                    return r.iter_lines()
                else:
                    return r.json()
            except Exception as e:
                return f"Error: {e}"
            
        
