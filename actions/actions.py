# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet,EventType
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .database import DataUpdate

class ActionName(Action):

    def name(self) -> Text:
        return "action_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name=''
        for ele in tracker.latest_message['entities']:
            if ele['entity']=='PERSON':
                name = name.join(ele['value'])
                print(name)
        print(tracker.latest_message['entities'])
        print(tracker.get_slot('name'))
        print(tracker.get_slot('PERSON'))
        print(tracker.sender_id)
        dispatcher.utter_message(template="utter_name",
                                 name=name)
        # dispatcher.utter_message(template="utter_ask_email")
        return [SlotSet("name", name if name is not None else 'bb')]

class ActionEmail(Action):

    def name(self) -> Text:
        return "action_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print(tracker.latest_message['entities'])
        email=tracker.get_slot('email')
        dispatcher.utter_message(template="utter_email",
                                 email=email)

        return [SlotSet("email", email)]

class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name=tracker.get_slot('name')
        email=tracker.get_slot('email')
        id=tracker.sender_id
        dispatcher.utter_message(template="utter_credentials",
                                 name=name,
                                 email=email,
                                 id=id)
        DataUpdate(name,email)
        return []