from typing import Dict, Text, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import operator


class ActionCalculate(Action):

    def name(self) -> Text:
        return "action_calculate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        operand1 = tracker.get_slot('operand1')
        operand2 = tracker.get_slot('operand2')
        operation = tracker.get_slot('operation')

        if operation == 'addition':
            result = operator.add(float(operand1), float(operand2))
        elif operation == 'subtraction':
            result = operator.sub(float(operand1), float(operand2))
        else:
            result = 'unknown'

        dispatcher.utter_message(
            template='utter_result',
            operand1=operand1,
            operand2=operand2,
            operation=operation,
            result=result
        )

        return []
