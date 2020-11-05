import slack_sdk
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
import string
from datetime import datetime, timedelta
import time

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)

slack_event_adapter = SlackEventAdapter(
    os.environ['SIGNING_SECRET'],
    '/slack/events',
    app
)

client = slack_sdk.WebClient(token=os.environ['SLACK_TOKEN'])

# client.chat_postMessage(channel='#test', text='hello')

@slack_event_adapter.on('message')


if __name__ == "__main__":
    app.run(debug=True)
