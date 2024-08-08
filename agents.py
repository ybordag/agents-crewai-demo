from crewai import Agent
from textwrap import dedent
from langchain.llms import Ollama
from langchain_openai import ChatOpenAI


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class ExampleAgents:
    def __init__(self):
        self.ollama = Ollama(model="crewai-llama3")

    def example_agent(self):
        return Agent(
            role=dedent(
                        """
                        Entity Extractor Agent - you extract information about entities you encounter 
                        in text
                        """
                    ),
            backstory=dedent(
                        """
                        You are excellent at detecting entities in text.
                        **attention to detail**
                        You are thorough in looking for nouns and entities in text and you are always 
                        able to find each one
                        **sparse**
                        You make sure to only return one entry per entity.
                        """
                    ),
            goal=dedent(f"""you extract entities from text and return each one as a JSON object"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.ollama,
        )


   
