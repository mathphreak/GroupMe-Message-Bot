import os
import requests
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask
from flask import request
app = Flask(__name__)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def post_Text(user_Text, bot_id):
    requests.post('https://api.groupme.com/v3/bots/post', params = {'bot_id' : bot_id, 'text' : user_Text})

@app.route('/callback/<bot_id>', methods=['POST'])
def parse_messages():
    message = request.get_json()
    if message['sender_type'] != "user":
        return 'OK'

    # BUPD Things
    if request.args.get('bupd', 'off') == 'on':
        # Johnny Law
        if "bupd" in message['text'].lower():
            post_Text("JOHNNY LAW", bot_id)

    # Say hello to anyone that says "Hi"
    if "Hi" in message['text']:
        post_Text("Hi " + message['name'].split(" ")[0] + "!", bot_id)

    """
    # Get annoyed at long texts
    if len(message['text']) >= 300:
        post_Text("Cool story bro.")
        """


    return 'OK'
