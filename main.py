from typing import List
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch


# object to describe the source tha tthe agent use to ge the answer
#l'objet hérite de la classe BaseModel
class Source(BaseModel):
    """Schema for the source used by the agent"""
    url:str = Field(description="The url of the source")

class AgentResponse(BaseModel):
    """Schema for the response returned by the agent"""

    answer:str = Field(description="The answer to the question")
    sources:List[Source] = Field(default_factory=list, description="The list of sources used to answer the question")


llm = ChatOpenAI(model="gpt-5")
tools=[TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="search for 3 job posting for an ai engineer using langchain in the bay area on linkedin and list their details")]})
    print(result)
   

if __name__ == "__main__":
    main()
