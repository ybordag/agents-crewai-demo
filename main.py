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

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = ExampleAgents()
        tasks = ExampleTasks()

        # Define your custom agents and tasks here
        example_agent = agents.example_agent()

        # Custom tasks include agent name and variables as input
        example_task = tasks.example_task(
            example_agent,
            self.var1,
            self.var2,
        )


        # Define your custom crew here
        crew = Crew(
            agents=[example_agent],
            tasks=[example_task],
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

    custom_crew = CustomCrew(var1, var2)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
