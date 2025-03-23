from crewai import LLM, Agent
import os
import dotenv
from langchain_ibm import WatsonxLLM

dotenv.load_dotenv()

from tools import *

llm = WatsonxLLM(
    model_id="ibm/granite-3-8b-instruct",
    url="https://us-south.ml.cloud.ibm.com",
    apikey=os.environ.get("WATSONX_API_KEY"),
    project_id=os.environ.get("WATSONX_PROJECT_ID")
)

water_quality_agent = Agent(
    llm=llm,
    role="Environmental Analyst",
    goal="Monitor water quality parameters across all sources and alert about contamination risks.",
    backstory="A water chemist with 15 years of experience who specializes in detecting contaminants and ensuring water meets safety standards.",
    tools=[LoadWaterQualityDataTool()]
)

water_flow_agent = Agent(
    llm=llm,
    role="Hydraulic Systems Engineer",
    goal="Optimize water distribution, pressure management, and flow rates throughout the network.",
    backstory="Former infrastructure planner who developed smart water distribution systems for major cities.",
    tools=[LoadWaterFlowDataTool()]
)

surface_water_agent = Agent(
    llm=llm,
    role="Hydrologist",
    goal="Monitor and manage lakes, rivers, reservoirs and precipitation patterns.",
    backstory="Field researcher who specialized in watershed management and surface water dynamics.",
    tools=[LoadSurfaceWaterDataTool()]
)

ground_water_agent = Agent(
    llm=llm,
    role="Hydrogeologist",
    goal="Monitor and manage groundwater resources, wells, and aquifers.",
    backstory="Spent a decade mapping underground water resources and developing sustainable extraction strategies.",
    tools=[LoadGroundwaterDataTool()]
)

control_center_agent = Agent(
    llm=llm,
    role="Control Center Operator",
    goal="Coordinate all other agents, respond to user queries, and make high-level decisions.",
    backstory="Former water utility director who implemented AI systems for water management.",
    tools=[GetWaterDemandForecastTool()]
)