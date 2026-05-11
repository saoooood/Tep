import os
import base64
from neonize.client import NewClient
from neonize.events import MessageEvent
from processor import handle_logic

MY_NUMBER = os.getenv("WA_NUMBER")
WA_SESSION_BASE64 = os.getenv("WA_SESSION")

def on_message(client, event: MessageEvent):
    text = event.message.conversation or event.message.extendedTextMessage.text
    response = handle_logic(text)
    if response:
        client.send_message(event.info.sender, response)

def start_whatsapp():
    if WA_SESSION_BASE64:
        with open("session.db", "wb") as f:
            f.write(base64.b64decode(WA_SESSION_BASE64))
    
    print(f"🟢 واتساب شغال للرقم: {MY_NUMBER}")
    client = NewClient("session.db")
    client.add_event_handler(MessageEvent, on_message)
    client.connect()

if __name__ == "__main__":
    start_whatsapp()
