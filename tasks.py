from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class ExampleTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def example_task(self, agent, var1, var2):
        return Task(description=dedent(
                        f"""
                        You extract entities and return each entity as a JSON object. Make sure to 
                        extract all entities but only return one entry per entity.

                        ***Steps to Complete Task***:
                        Evaluate each noun in the text to see if it is a new entity
                        If it is a new entity, create a new entry and add important information 
                        as properties in the JSON.
                        If the user has provided any properties which need to be extracted, 
                        prioritize extracting that information.
                        
                        {self.__tip_section()}
                
                        Make sure to use the following data.
                
                        Text: {var1}
                        Properties: {var2}
                        """
                    ),
                agent=agent,
                expected_output=dedent(
                        f"""***Output Format***: 
                        Return output in well formatted JSON

                        **Input 1:**
                        ```
                        Text: "John Smith, CEO of XYZ Corporation, met with Jane Doe, a prominent 
                        investor."
                        ```

                        **Output 1:**
                        ```
                        [
                            {{
                                "entity": "John Smith",
                                "type": "person",
                                "position": "CEO"
                            }},
                            {{
                                "entity": "Jane Doe",
                                "type": "person",
                                "occupation": "investor"
                            }}
                        ]
                        ```

                        **Input 2:**
                        ```
                        Text: "The new product, codenamed 'Aurora', will be released next 
                        quarter."
                        ```

                        **Output 2:**
                        ```
                        [
                            {{
                                "entity": "Aurora",
                                "type": "product",
                                "codename": true
                            }}
                        ]
                        ```

                        **Input 3:**
                        ```
                        Text: "The company is headquartered in New York City and has offices in 
                        San Francisco and London."
                        ```

                        **Output 3:**
                        ```
                        [
                            {{
                                "entity": "New York City",
                                "type": "location"
                            }},
                            {{
                                "entity": "San Francisco",
                                "type": "location"
                            }},
                            {{
                                "entity": "London",
                                "type": "location"
                            }}
                        ]
                        ```

                        **Input 4:**
                        ```
                        Text: "The report highlights the importance of data security and mentions 
                        recent breaches at Apple and Facebook."
                        ```

                        **Output 4:**
                        ```
                        [
                            {{
                                "entity": "Apple",
                                "type": "organization"
                            }},
                            {{
                                "entity": "Facebook",
                                "type": "organization"
                            }}
                        ]
                        ```

                        """
                    )
                )

