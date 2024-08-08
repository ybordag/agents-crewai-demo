from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class ExampleTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def extraction_task(self, agent, var1, var2):
        return Task(description=dedent(
                        f"""
                        You extract entities and return each entity as a JSON object. Make sure to 
                        extract all entities but only return one entry per entity.

                        **Steps to Complete Task**:
                        1. Evaluate each noun in the text to determine if it represents a new 
                        entity or not.
                        2. For each new entity, create a new JSON entry and add relevant details 
                        as properties.
                        3. If user-provided properties are specified, prioritize extracting that 
                        information to provide a more comprehensive understanding.
                        
                        {self.__tip_section()}
                
                        **Important Information**:
                        Make sure to use the following data.
                        * Text: {var1}
                        * Properties: {var2}
                        """
                    ),
                agent=agent,
                expected_output=dedent(
                        f"""***Output Format***: 
                        Return output in well formatted JSON

                        **Example Input 1:**
                        ```
                        Text: "John Smith, CEO of XYZ Corporation, met with Jane Doe, a prominent 
                        investor."
                        ```

                        **Example Output 1:**
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

                        **Example Input 2:**
                        ```
                        Text: "The report highlights the importance of data security and mentions 
                        recent breaches at Apple and Facebook."
                        ```

                        **Example Output 2:**
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

                        **Example Input 3:**
                        ```
                        Text: "Recent studies have shown that the development of artificial 
                        intelligence (AI) has significant implications for the field of psychology. 
                        For instance, AI-powered chatbots are being used to diagnose mental health 
                        disorders with increased accuracy, leading to a reevaluation of traditional 
                        therapeutic approaches. Furthermore, researchers are exploring the 
                        potential benefits of AI-assisted cognitive training for individuals with 
                        neurodevelopmental disorders such as autism spectrum disorder (ASD). The 
                        integration of AI in these areas has also sparked discussions about the 
                        role of human judgment and bias in decision-making processes."
                        ```

                        **Example Output 3:**
                        ```
                        [
                            {{
                                "name": "artificial intelligence (AI)", 
                                "type": "concept"
                            }},
                            {{
                                "name": "psychology", 
                                "type": "field"
                            }},
                            {{
                                "name": "AI-powered chatbots", 
                                "type": "technology"
                            }},
                            {{
                                "name": "mental health disorders", 
                                "type": "condition"
                            }},
                            {{
                                "name": "neurodevelopmental disorders (ASD)", 
                                "type": "condition"
                            }},
                            {{
                                "name": "AI-assisted cognitive training", 
                                "type": "approach"
                            }},
                            {{
                                "name": "human judgment and bias", 
                                "type": "concept"
                            }},
                            {{
                                "name": "decision- Making processes", 
                                "type": "process"
                            }}
                        ]
                        ```

                        *DO NOT INCLUDE EXAMPLES IN YOUR RESPONSE*
                        """
                    )
                )
    
    def connecting_task(self, agent, var1, var3):
        return Task(description=dedent(
                        f"""
                        You connect entities and return each connection as a JSON object. Make sure 
                        to identify all relevant connections between entities, including those 
                        specified by the user.

                        **Steps to Complete Task**:
                        1. Evaluate each pair of entities outputed from the Extractor Agent in the 
                        text to determine if they represent a new connection or not.
                        2. For each new connection, create a new JSON entry and add relevant 
                        details as properties.
                        3. If user-specified relationships are provided, prioritize identifying 
                        connections that match those relationships to provide a more comprehensive 
                        understanding.
                        4. Copy the Entity List returned by the extraction agent
                        5. RETURN BOTH THE ENTITY LIST AND RELATIONSHIPT LIST!!
                        
                        {self.__tip_section()}
                
                        **Important Information**:
                        Make sure to use the following data.
                        * Text: {var1}
                        * Relationships: {var3}
                        """
                    ),
                agent=agent,
                expected_output=dedent(
                        f"""***Output Format***: 
                        Return BOTH THE ENTITY LIST AND RELATIONSHIPT LIST output in well formatted 
                        JSON

                        **Example Input 1:**
                        ```
                        Text: "John Smith, CEO of XYZ Corporation, met with Jane Doe, a prominent 
                        investor."
                        
                        Entities:
                        [
                            {{
                                "entity": "John Smith",
                                "type": "person",
                                "position": "CEO"
                            }},
                            {{
                                "entity": "XYZ Corporation",
                                "type": "company"
                            }},
                            {{
                                "entity": "Jane Doe",
                                "type": "person",
                                "occupation": "investor"
                            }}
                        ]
                        ```

                        **Example Output 1:**
                        ```
                        {{
                            "Entities": [
                                {{
                                    "entity": "John Smith",
                                    "type": "person",
                                    "position": "CEO"
                                }},
                                {{
                                    "entity": "XYZ Corporation",
                                    "type": "company"
                                }},
                                {{
                                    "entity": "Jane Doe",
                                    "type": "person",
                                    "occupation": "investor"
                                }}
                            ],
                            "Relationships": [
                                {{
                                    "relationship": "acquaintance",
                                    "entity 1": "John Smith",
                                    "entity 2": "Jane Doe"
                                }},
                                {{
                                    "relationship": employee",
                                    "entity 1": "John Smith",
                                    "entity 2": "XYZ Corporation",
                                    "position": "CEO"
                                }}
                            ]
                        }}
                        ```

                        **Example Input 2:**
                        ```
                        Text: "Recent studies have shown that the development of artificial 
                        intelligence (AI) has significant implications for the field of psychology. 
                        For instance, AI-powered chatbots are being used to diagnose mental health 
                        disorders with increased accuracy, leading to a reevaluation of traditional 
                        therapeutic approaches. Furthermore, researchers are exploring the 
                        potential benefits of AI-assisted cognitive training for individuals with 
                        neurodevelopmental disorders such as autism spectrum disorder (ASD). The 
                        integration of AI in these areas has also sparked discussions about the 
                        role of human judgment and bias in decision-making processes."
                        
                        Entities:
                        [
                            {{
                                "name": "artificial intelligence (AI)", 
                                "type": "concept"
                            }},
                            {{
                                "name": "psychology", 
                                "type": "field"
                            }},
                            {{
                                "name": "AI-powered chatbots", 
                                "type": "technology"
                            }},
                            {{
                                "name": "mental health disorders", 
                                "type": "condition"
                            }},
                            {{
                                "name": "neurodevelopmental disorders (ASD)", 
                                "type": "condition"
                            }},
                            {{
                                "name": "AI-assisted cognitive training", 
                                "type": "approach"
                            }},
                            {{
                                "name": "human judgment and bias", 
                                "type": "concept"
                            }},
                            {{
                                "name": "decision- Making processes", 
                                "type": "process"
                            }}
                        ]
                        ```

                        **Example Output 2:**
                        ```
                        {{
                            "Entities": [
                                {{
                                    "name": "artificial intelligence (AI)", 
                                    "type": "concept"
                                }},
                                {{
                                    "name": "psychology", 
                                    "type": "field"
                                }},
                                {{
                                    "name": "AI-powered chatbots", 
                                    "type": "technology"
                                }},
                                {{
                                    "name": "mental health disorders", 
                                    "type": "condition"
                                }},
                                {{
                                    "name": "neurodevelopmental disorders (ASD)", 
                                    "type": "condition"
                                }},
                                {{
                                    "name": "AI-assisted cognitive training", 
                                    "type": "approach"
                                }},
                                {{
                                    "name": "human judgment and bias", 
                                    "type": "concept"
                                }},
                                {{
                                    "name": "decision- Making processes", 
                                    "type": "process"
                                }}
                            ],
                            "Relationships": [
                                {{ 
                                    "relationship": "implication", 
                                    "entity 1": "artificial intelligence (AI)",
                                    "entity 2": "psychology"
                                }},
                                {{ 
                                    "relationship": "application", 
                                    "entity 1": "AI-powered chatbots",
                                    "entity 2": "mental health disorders"
                                }},
                                {{ 
                                    "relationship": "exploration", 
                                    "entity 1": "AI-assisted cognitive training",
                                    "entity 2": "neurodevelopmental disorders (ASD)"
                                }},
                                {{ "relationship": "discussion", 
                                    "entity 1": "human judgment and bias",
                                    "entity 2": "decision-making processes"
                                }}
                            ]
                        }}
                        ```

                        *DO NOT INCLUDE EXAMPLES IN YOUR RESPONSE*
                        """
                    )
                )

