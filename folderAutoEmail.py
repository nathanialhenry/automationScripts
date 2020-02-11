# TODO add path to watchDirectory, add Slack integration
import requests
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import json
import argparse

# Get Argument for SLACK Token
parser = argparse.ArgumentParser(description="needed for copying the slack token")
parser.add_argument("--token", type=str, help="copy your slack token here")
parser.add_argument("--path", type=str, help="copy desired folder path here")
parser.add_argument("--channel", type=str, help="copy your desired slack channel here")
parser.add_argument("--bot", type=str, help="copy your desired slack bot name here")

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

# create observer class
class OnMyWatch:
    # Set the directory on watch
    watchDirectory = args.path

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(10)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()

# creates event handler class
class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Event is created, you can process it now
            slack_info = "This is a BOT: I have detected {0} has been added to the Share Folder used by QV (most likely a build). You can find this added file/folder here: {1}".format(event.src_path, watchDirectory)
            post_message_to_slack(slack_info)

        elif event.event_type == 'modified':
            # Event is modified, you can process it now
            slack_info = "This is a BOT: I have detected {0} has been modified in the Share Folder used by QV (most likely a build). You can find this added file/folder here: {1}".format(event.src_path, watchDirectory)
            post_message_to_slack(slack_info)


if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()

