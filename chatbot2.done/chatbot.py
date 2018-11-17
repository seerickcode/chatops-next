import os
import time
from slackclient import SlackClient

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

if sc.rtm_connect():
    print("Connected and watching")
    while sc.server.connected is True:
        messages = sc.rtm_read()
        if len(messages):
            for message in messages:
                print("{}\n".format(message))
                if ( message.get('type') == 'message' and
                        'rabbit' in message.get('text', "")):
                    sc.rtm_send_message(message['channel'],"RUN!! :runner:")

        time.sleep(1)
else:
    print("Connection Failed")

