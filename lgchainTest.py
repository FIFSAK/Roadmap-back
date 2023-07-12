from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import OpenAI
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

llm = OpenAI(temperature=0)

# tools = load_tools(["serpapi", "llm-math"], llm=llm)

# agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)


def search_links_lch(response):
    query = llm.predict(
        f"""
            Context: you will be provided with a roadmap based on it, provide links to resources where you can study the topics prescribed in the roadmap
            Roudmap:{response}
            Answer: max_tokens=200"""
    )
    print("LINKS CREATED")
    print(query)
    return query


