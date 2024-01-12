import requests
import time
import json
import os
from dotenv import load_dotenv
from urllib import parse, request
from googletrans import Translator

load_dotenv()

BOT_ID = os.getenv("BOT_ID")
GROUP_ID = os.getenv("GROUP_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
LAST_MESSAGE_ID = None


def send_message(text, attachments=None):
    """Send a message to the group using the bot."""
    post_url = "https://api.groupme.com/v3/bots/post"
    data = {"bot_id": BOT_ID, "text": text, "attachments": attachments or []}
    response = requests.post(post_url, json=data)
    return response.status_code == 202


def get_group_messages(since_id=None):
    """Retrieve recent messages from the group."""
    params = {"token": ACCESS_TOKEN}
    if since_id:
        params["since_id"] = since_id

    get_url = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages"
    response = requests.get(get_url, params=params)
    if response.status_code == 200:
        # this shows how to use the .get() method to get specifically the messages but there is more you can do (hint: sample.json)
        return response.json().get("response", {}).get("messages", [])
    return []


def process_message(message):
    """Process and respond to a message."""
    global LAST_MESSAGE_ID
    text = message["text"].lower()
    sender_id = message["sender_id"]
    sender_type = message["sender_type"]
    name = message["name"]

    # i.e. responding to a specific message (note that this checks if "hello bot" is anywhere in the message, not just the beginning)

    if sender_id == "40293401" and "good morning" not in text and "good night" not in text and sender_type != "bot" and "sticker" not in text and "translate" not in text:
        send_message("ReeBot here!")
    elif sender_type != "bot": # filter out bot senders
        if "good morning" in text: 
            send_message("Good morning " + name)
        elif "good night" in text:
            send_message("Good night " + name)
        elif "sticker" in text:
            content = text.split(" ")[-1]
            giphy_endpoint = "http://api.giphy.com/v1/stickers/search"
            parameters = parse.urlencode({
                "q": content, 
                "api_key": "iRyCTPbjHA647357911tLIU6RtMnzRKa", 
                "limit": "5", 
                "rating": "g", 
                "lang": "en"})

            with request.urlopen("".join((giphy_endpoint, "?", parameters))) as response:
                sticker = json.loads(response.read())

            if sticker:
                sticker_url = sticker["data"][0]["embed_url"]
                send_message(sticker_url)
            else:
                send_message("Sorry, no sticker found.", [])
        elif "translate" in text:
            lang = text.split(" ")[-1]
            map = {"spanish": "es", "french": "fr", "japanese": "ja", "mandarin": "zh-CN", "korean": "ko", "hindi": "hi"}
            content = "".join([element.strip("\"") for element in text.split(" ")[1:-2]])
            if content.startswith("translate"):
                content = content[9:]
            translator = Translator()
            translation = translator.translate(content, dest = map[lang])
            send_message(translation.text)

    LAST_MESSAGE_ID = message["id"]


def main():
    global LAST_MESSAGE_ID
    # this is an infinite loop that will try to read (potentially) new messages every 10 seconds, but you can change this to run only once or whatever you want
    while True:
        messages = get_group_messages(LAST_MESSAGE_ID)
        for message in reversed(messages):
            process_message(message)
        time.sleep(10)


if __name__ == "__main__":
    main()
