import json, os
import requests
from dotenv import load_dotenv
import boto3

load_dotenv()
WEBHOOK_URL = os.environ['WEBHOOK_URL']

# Message { text: string, attachments: Attachment[] }
# Attachment { filename: string, base64: string }
def send_message(message):
    # formats message -> data
    headers = { "Content-Type": "application/json" }
    data = { "content": message["text"] }
    json_data = json.dumps(data)
    response = requests.post(WEBHOOK_URL, headers=headers, data=json_data)
    print(response)

def send_announcement(announcement):
    for message in announcement: send_message(message)

# Clean Up
def delete_rule(id):
    print("Deleting Rule ID", id)
    client = boto3.client('events')
    
    rule_targets = client.list_targets_by_rule(Rule=id)['Targets']
    target_ids = [target['Id'] for target in rule_targets]
    
    remove_targets_response = client.remove_targets(Rule=id, Ids=target_ids)
    print(remove_targets_response)
    
    delete_rule_response = client.delete_rule(Name=id)
    print(delete_rule_response)

# Entry Point
# Triggered by EventBridge Rule
def lambda_handler(event, context):
    print("Event: ", event)
    print("Context: ", context)
    
    if event is None:
        print("Event is empty")    
        return
    
    if "announcement" not in event or "id" not in event:
        print("Event missing required keys `announcement` and/or `id`")
        return

    send_announcement(event["announcement"])
    delete_rule(event["id"])

    return "Hello from 1Announce Discord Lambda ✨"