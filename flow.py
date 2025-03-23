from crewai import Agent, Crew, Task, LLM
from crewai_tools import SerperDevTool
import dotenv
import os
dotenv.load_dotenv()

from tasks import *
from agents import *



crew = Crew(
    agents=[
        water_quality_agent,
        water_flow_agent,
        surface_water_agent,
        ground_water_agent,
        control_center_agent,
    ],
    tasks=[
        water_quality_task,
        water_flow_task,
        surface_water_task,
        groundwater_task,
        control_center_task,
    ],
    verbose=True
)

results = crew.kickoff()
print(results)
