import time
from neonize.client import NewClient
from neonize.events import MessageEvent
from processor import handle_logic # استدعاء المعالج المركزي

def on_message(client, event: MessageEvent):
    # الحصول على نص الرسالة
    text = event.message.conversation or event.message.extendedTextMessage.text
    
    # إرسال النص للمعالج (سعيد ثون)
    response = handle_logic(text)
    
    # إذا وجد المعالج رداً، يتم إرساله للواتساب
    if response:
        client.send_message(event.info.sender, response)

def start_whatsapp():
    print("🟢 جاري تشغيل سعيد ثون على واتساب...")
    # هنا ستحتاج لمسح الكود (QR Code) عند أول تشغيل في سجلات (Logs) الـ GitHub
    client = NewClient("db.sqlite3")
    client.add_event_handler(MessageEvent, on_message)
    client.connect()

if __name__ == "__main__":
    start_whatsapp()
