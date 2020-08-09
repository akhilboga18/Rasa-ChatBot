# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionPythonFirstCustomCode(Action):

    def name(self) -> Text:
        return "action_python_custom"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Python custom code is called and it is working fine!")

        return []
        
class SearchDocumentationforTesting(Action):

    def name(self) -> Text:
        return "action_searchdoc_test"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
            entities = tracker.latest_message['entities']
            print(entities)
            
            for e in entities:
                if e['entity'] == 'testing':
                    name = e['value']
                
                if name == "OAT":
                    message = "Doc1 for OAT,Doc2 for OAT,Doc3 for OAT"
                
                if name == "UAT":
                    message = "Doc1 for UAT,Doc2 for UAT,Doc3 for UAT"
                
                if name == "Production":
                    message = "Doc1 for Production,Doc2 for Production,Doc3 for Production"
                
                
            dispatcher.utter_message(text=message)

            return []
            
            
class SearchDocumentationforChanges(Action):

    def name(self) -> Text:
        return "action_searchdoc_changes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
            entities = tracker.latest_message['entities']
            print(entities)
            
            for e in entities:
                if e['entity'] == 'change_request':
                    name = e['value']
                
                if name == "high":
                    message = "Doc1 for high,Doc2 for high,Doc3 for high"
                
                if name == "medium":
                    message = "Doc1 for medium,Doc2 for medium,Doc3 for medium"
                
                if name == "low":
                    message = "Doc1 for low,Doc2 for low,Doc3 for low"
                
                
            dispatcher.utter_message(text=message)

            return []
            
            
            
class ActionSlot(Action):

     def name(self) -> Text:
         return "action_slot"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             
         name = tracker.get_slot("name")
         message = " {} is the name captured in actions py file".format(name)
         print(message)

         dispatcher.utter_message(message)

         return []
         
class TestingDefinitions(Action):

    def name(self) -> Text:
        return "action_testing_def"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
            entities = tracker.latest_message['entities']
            print(entities)
            
            for e in entities:
                if e['entity'] == 'testing':
                    name = e['value']
                
                if name == "OAT":
                    message = "Operational acceptance testing (OAT) is used to conduct operational readiness (pre-release) of a product, service, or system as part of a quality management system."
                
                if name == "UAT":
                    message = "User Acceptance Testing (UAT): The main purpose of this testing is to validate the software against the business requirements. This validation is carried out by the end-users who are familiar with the business requirements."
                
                if name == "SIT":
                    message = "System Integration Testing is defined as a type of software testing carried out in an integrated hardware and software environment to verify the behavior of the complete system. It is testing conducted on a complete, integrated system to evaluate the system's compliance with its specified requirement."
                
                
            dispatcher.utter_message(text=message)

            return []