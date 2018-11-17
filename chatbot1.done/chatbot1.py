import os
from slackclient import SlackClient

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

# Get the group channels with the following
# for group in sc.api_call("groups.list").get("groups"):
#    print("{}-{}".format(group['id'],group['name']))

sc.api_call(
  "chat.postMessage",
  channel="GDZULG3U0",
  text="Hello from Python! :tada:"
)
