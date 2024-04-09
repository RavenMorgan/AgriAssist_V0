from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionGetWeather(Action):
       def name(self) -> Text:
        return "action_get_weather_forecast"

       def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        message = """Weather forecasts are typically available through local meteorological services or online weather platforms. You can check weather forecasts for Benguerir to determine if rain is expected tomorrow."""
        
        dispatcher.utter_message(text=message)

        return []
    #     def get_weather(self, location: Text) -> Dict[Text, Any]:
    #     api_key = "36846ba4cc899361b6eabdc096d68296"
    #     url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    #     response = requests.get(url)
    #     if response.status_code == 200:
    #         return response.json()
    #     else:
    #         return None
        
    # def log_conversation(self, events: List[Dict[Text, Any]]):
    #    Log conversation events to your desired location or database
    #    to store conversation events in a file, database, or any other storage medium
    #    Example: I write the events to a log file
    #     with open("conversation.log", "a") as log_file:
    #         for event in events:
    #             log_file.write(f"{event}\n")

import os


class ActionAskYield(Action):
    def name(self) -> Text:
        return "action_provide_yield_infos"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
       
        message = """Small potatoes at harvest can be due to several factors, including overcrowding, inadequate spacing between plants, shallow planting depth, poor soil fertility, or insufficient watering. To improve potato yield, ensure proper spacing between plants, plant them at the correct depth, provide adequate nutrients through fertilization, and maintain consistent soil moisture levels."""
        dispatcher.utter_message(text=message)

        return []
    

    # def fetch_gooey_response(self, input_prompt: Text) -> Dict[Text, Any]:
    #     api_key = os.getenv("GOOEY_API_KEY")
    #     if api_key is None:
    #         raise Exception("GOOEY_API_KEY is not set. Please check your environment variables.")

    #     payload = {"input_prompt": input_prompt}

    #     try:
    #         response = requests.post(
    #             "https://api.gooey.ai/v2/video-bots/",
    #             headers={"Authorization": "Bearer " + api_key},
    #             json=payload,
    #         )
    #         if not response.ok:
    #             raise Exception(f"API request failed with status code {response.status_code}: {response.content}")

    #         return response.json()
    #     except Exception as e:
    #         print(f"An error occurred while making the API request: {e}")
    #         return {"Response": "Sorry, I couldn't fetch the response."}

    #     return {}
class ActionAskMarketInformation(Action):
    def name(self) -> Text:
        return "action_provide_market_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = """For red potatoes, popular seed varieties include Red Pontiac, Norland, and Red La Soda. These varieties are known for their good yield, disease resistance, and excellent taste."""
        dispatcher.utter_message(text=message)

        return []

class ActionAskPestControl(Action):
    def name(self) -> Text:
        return "action_Pest_control"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Use Gooey AI API to fetch response for Pest_control intent
        message =  """Pest-resistant varieties of wheat include Triticum aestivum (common wheat) cultivars such as 'Gallant,' 'Apache,' and 'Westbred 926.' These varieties exhibit resistance to common wheat pests such as aphids, Hessian flies, and powdery mildew."""
        dispatcher.utter_message(text=message)

        return []


class ActionAskIrrigationFertilization(Action):
    def name(self) -> Text:
        return "action_provide_irrigation_fertilization"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Use Gooey AI API to fetch response for irrigation_fertilization intent
        message = """Irrigation techniques suitable for arid regions include drip irrigation, which delivers water directly to the plant roots, reducing water loss through evaporation; micro-sprinkler irrigation, which provides a fine mist of water; and using moisture-retaining mulches to reduce water evaporation from the soil surface."""
        dispatcher.utter_message(text=message)

        return []

