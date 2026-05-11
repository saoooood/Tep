import os
import base64
from neonize.client import NewClient
# تم تغيير المسار هنا ليناسب النسخة الجديدة
from neonize.types import Message
from processor import handle_logic

MY_NUMBER = os.getenv("WA_NUMBER")
WA_SESSION_BASE64 = os.getenv("WA_SESSION")

def on_message(client, message: Message):
    # الحصول على نص الرسالة
    text = message.text
    response = handle_logic(text)
    if response:
        client.send_message(message.chat, response)

def start_whatsapp():
    if WA_SESSION_BASE64:
        with open("session.db", "wb") as f:
            f.write(base64.b64decode(WA_SESSION_BASE64))
    
    client = NewClient("session.db")
    # تعديل طريقة استقبال الرسائل
    client.message_handler(on_message)
    print(f"🟢 واتساب شغال: {MY_NUMBER}")
    client.connect()

if __name__ == "__main__":
    start_whatsapp()
