# from langchain.agents import AgentType, initialize_agent, load_tools
# from langchain.llms import OpenAI
# from langchain.chat_models import ChatOpenAI
import os
import dotenv
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
dotenv.load_dotenv(dotenv.find_dotenv())
import asyncio
from langchain.callbacks.streaming_aiter import AsyncIteratorCallbackHandler

llm = ChatOpenAI(
   model = "gpt-3.5-turbo" ,
   openai_api_key = os.getenv("OPENAI_API_KEY"),
   streaming=True,
   callbacks=[StreamingStdOutCallbackHandler()] 
)

def search_links_lch(response):
    async def generate_links():
        query = f"""
            Context: you will be provided with a roadmap based on it, provide links to resources where you can study the topics prescribed in the roadmap find for all topics and complete response
            Roudmap:{response}
            """

        for resp in llm.predict(query, stream=True):
            yield resp
    return generate_links()

# llm.predict('who are you')