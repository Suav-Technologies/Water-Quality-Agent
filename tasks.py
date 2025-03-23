from crewai import Task

from agents import *


water_quality_task = Task(
    description="""
    Analyze current water quality data from all sources.
    1. Check if any parameters exceed safety thresholds
    2. Identify which water source has the best overall quality
    3. Recommend any necessary treatment actions for problematic sources
    4. Prepare a brief quality assessment report
    
    The safety thresholds are:
    - pH: between 6.5 and 8.5
    - Turbidity: below 1.0 NTU
    - Dissolved oxygen: above 6.0 mg/L
    - E. coli: below 10 CFU/100mL
    """,
    agent=water_quality_agent,
    expected_output="A comprehensive water quality assessment report with recommendations"
)

water_flow_task = Task(
    description="""
    Analyze the current flow and pressure data in the distribution network.
    1. Identify any potential leaks or pressure issues
    2. Recommend pump scheduling to optimize energy usage
    3. Suggest flow adjustments to meet expected demand
    4. Prioritize any required maintenance actions
    
    Optimal pressure range is 55-65 psi.
    Energy usage should be minimized while maintaining service.
    """,
    agent=water_flow_agent,
    expected_output="A flow optimization report with specific recommendations for each district"
)

surface_water_task = Task(
    description="""
    Evaluate all surface water sources and their current status.
    1. Determine if any reservoirs or lakes are at critical levels
    2. Based on precipitation forecasts, predict changes over the next 72 hours
    3. Recommend optimal withdrawal rates from each source
    4. Flag any concerns about flood or drought conditions
    
    Critical level for reservoirs is below 30% or above 95% capacity.
    """,
    agent=surface_water_agent,
    expected_output="A surface water status report with 72-hour projections and recommendations"
)

groundwater_task = Task(
    description="""
    Assess the current state of all groundwater resources.
    1. Compare extraction rates with recharge rates for each aquifer
    2. Identify any unsustainable usage patterns
    3. Recommend sustainable pumping schedules
    4. Suggest any necessary recharge activities
    
    Sustainable extraction means extraction rate ≤ recharge rate.
    Well water depths should not increase by more than 1% per month.
    """,
    agent=ground_water_agent,
    expected_output="A groundwater sustainability report with specific recommendations"
)

control_center_task = Task(
    description="""
    Coordinate and optimize the entire water system based on inputs from all other agents.
    1. Review the outputs from the water quality, flow, surface water, and groundwater agents
    2. Match water demand forecast with available supply from all sources
    3. Prioritize highest quality water sources while maintaining sustainability
    4. Develop an integrated 24-hour operations plan
    5. Identify any critical issues requiring immediate attention
    
    Energy usage should be minimized while maintaining water quality and meeting demand.
    """,
    agent=control_center_agent,
    context=[water_quality_task, water_flow_task, surface_water_task, groundwater_task],
    expected_output="A comprehensive 24-hour water system operations plan"
)