import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import re
#Intialization of the authenticator and assistant
authenticator = IAMAuthenticator('HEogUwkxOj-K3Oj92z6XcOO_K6_Nhj2J-nSOL9y2_Q7G')
assistant = AssistantV2(
    version='2020-04-01',
    authenticator = authenticator
)
assistant.set_service_url('https://api.us-east.assistant.watson.cloud.ibm.com/instances/0ca2cd54-ee50-4c47-a0ed-88f4fdcf6971')
print("Welcome to Hermes! the insurance bot");
# asks questions and start of while loop
while(True):
    def toString(list):
        str1 = " "
        return (str1.join(list))
    intent = input("what would you like me to do? ")
    response = assistant.create_session(
        assistant_id='a75cc576-dffc-48a9-aca8-6355d2e1e26c'
    ).get_result()
    sessionCode = json.loads(json.dumps(response, indent = 2))
    print("Your session code is " + sessionCode['session_id'])
    questions = assistant.message(
    assistant_id='a75cc576-dffc-48a9-aca8-6355d2e1e26c',
    session_id= sessionCode['session_id'],
    input={'message_type': 'text', 'text': intent}
    ).get_result()


    output = json.loads(json.dumps(questions, indent=2))
    output = output['output']['generic']
    outputToString = str(output)
    splitString = outputToString.split(",")
    printingOutput = splitString[1].split(": '")
    print("Hermes says: " + printingOutput[1])
