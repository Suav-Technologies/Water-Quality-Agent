from crewai.tools import BaseTool

class LoadWaterQualityDataTool(BaseTool):
    name: str = "Load Water Quality Data"
    description: str = "Load water quality data from various sources."

    def _run(self) -> dict:
        return {
            "desalination_plant": {"ph": 7.2, "turbidity": 0.8, "dissolved_oxygen": 8.5, "e_coli": 0},
            "river": {"ph": 6.8, "turbidity": 2.3, "dissolved_oxygen": 7.2, "e_coli": 15},
            "lake": {"ph": 7.5, "turbidity": 1.5, "dissolved_oxygen": 8.1, "e_coli": 5},
            "groundwater": {"ph": 7.8, "turbidity": 0.4, "dissolved_oxygen": 6.5, "e_coli": 0},
            "treated_sewage": {"ph": 7.0, "turbidity": 1.2, "dissolved_oxygen": 7.8, "e_coli": 2}
        }

class LoadWaterFlowDataTool(BaseTool):
    name: str = "Load Water Flow Data"
    description: str = "Load water flow and pressure data from the distribution network."

    def _run(self) -> dict:
        return {
            "main_pump_station": {"flow_rate": 250, "pressure": 65, "energy_usage": 42},
            "north_district": {"flow_rate": 80, "pressure": 58, "leak_detection": False},
            "east_district": {"flow_rate": 65, "pressure": 61, "leak_detection": False},
            "south_district": {"flow_rate": 95, "pressure": 52, "leak_detection": True},
            "west_district": {"flow_rate": 75, "pressure": 60, "leak_detection": False}
        }

class LoadSurfaceWaterDataTool(BaseTool):
    name: str = "Load Surface Water Data"
    description: str = "Load data about surface water sources."

    def _run(self) -> dict:
        return {
            "main_reservoir": {"level": 82, "capacity": 100, "inflow": 12, "outflow": 15},
            "river_upstream": {"flow_rate": 120, "height": 3.2, "precipitation_forecast": 25},
            "lake_alpha": {"level": 65, "capacity": 100, "evaporation_rate": 2.2},
            "lake_beta": {"level": 45, "capacity": 100, "evaporation_rate": 2.5}
        }

class LoadGroundwaterDataTool(BaseTool):
    name: str = "Load Groundwater Data"
    description: str = "Load data about groundwater sources."

    def _run(self) -> dict:
        return {
            "aquifer_main": {"level": 75, "extraction_rate": 8, "recharge_rate": 6},
            "aquifer_secondary": {"level": 62, "extraction_rate": 5, "recharge_rate": 4},
            "well_cluster_north": {"depth_to_water": 85, "pumping_rate": 4.5, "water_quality": "good"},
            "well_cluster_south": {"depth_to_water": 92, "pumping_rate": 3.8, "water_quality": "fair"}
        }

class GetWaterDemandForecastTool(BaseTool):
    name: str = "Get Water Demand Forecast"
    description: str = "Get forecasted water demand for next 24 hours."

    def _run(self) -> dict:
        return {
            "morning_peak": 220,
            "midday": 180,
            "evening_peak": 240,
            "night": 120,
            "industrial_continuous": 85
        }