import os
import time
from instagrapi import Client
from processor import handle_logic

# جلب اليوزر والباسورد من الأسرار
USERNAME = os.getenv("INSTA_USER")
PASSWORD = os.getenv("INSTA_PASS")

def start_insta():
    client = Client()
    try:
        print("📸 تسجيل دخول انستا...")
        client.login(USERNAME, PASSWORD)
        print("✅ تم دخول انستا بنجاح!")
        last_check = time.time()
        while True:
            try:
                threads = client.direct_threads()
                for thread in threads:
                    if thread.unread_count > 0:
                        for message in thread.messages:
                            if message.timestamp.timestamp() > last_check:
                                reply = handle_logic(message.text)
                                if reply:
                                    client.direct_answer(thread.id, reply)
                last_check = time.time()
                time.sleep(30) # حماية من الحظر
            except Exception as e:
                time.sleep(60)
    except Exception as e:
        print(f"❌ فشل انستا: {e}")

if __name__ == "__main__":
    start_insta()
