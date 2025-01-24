from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

# from actions.db import add_contact, get_contacts, Contact

class ApplyFireNOC(Action):
    def name(self) -> str:
        return "connect_to_vrm"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]):  
        dispatcher.utter_message(text="Connecting to VRM...")
        return [SlotSet("return_value", "Success")]