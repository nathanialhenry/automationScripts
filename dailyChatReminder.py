import requests
import json
import time
import argparse

# Get Arguments
parser = argparse.ArgumentParser(description="needed for copying the slack token")
parser.add_argument("--token", type=str, help="copy your slack token here")
parser.add_argument("--channel", type=str, help="copy your slack channel here")
parser.add_argument("--bot", type=str, help="copy your slack bot name here")

args = parser.parse_args()

# Set Slack Variables
slack_token = args.token
slack_channel = args.channel
slack_bot_name = args.bot

# create slack function
def post_message_to_slack(text, blocks = None):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': text,
        'username' : slack_bot_name,
        'blocks': json.dumps(blocks) if blocks else None
    }).json()	


# create slack message and post to slack
slack_info = "I am a Bot: Is there anything that needs to be handed off or completed today? "
post_message_to_slack(slack_info)