import os
from crewai import Agent, Task, Crew, Process

from textwrap import dedent
from agents import ExampleAgents
from tasks import ExampleTasks


# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = ExampleAgents()
        tasks = ExampleTasks()

        # Define your custom agents and tasks here
        extractor_agent = agents.extractor_agent()
        connector_agent = agents.connector_agent()

        # Custom tasks include agent name and variables as input
        extraction_task = tasks.extraction_task(
            extractor_agent,
            self.var1,
            self.var2,
        )

        connecting_task = tasks.connecting_task(
            connector_agent,
            self.var1,
            self.var3
        )


        # Define your custom crew here
        crew = Crew(
            agents=[extractor_agent, connector_agent],
            tasks=[extraction_task, connecting_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    var1 = input(dedent("""Text to be extracted: """))
    var2 = input(dedent("""Properties to be extracted: """))
    var3 = input(dedent("""Relationships to be extracted: """))

    custom_crew = CustomCrew(var1, var2, var3)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
