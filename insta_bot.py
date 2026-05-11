import os
from instagrapi import Client
from processor import handle_logic

# القراءة من GitHub Secrets
USERNAME = os.getenv("INSTA_USER")
PASSWORD = os.getenv("INSTA_PASS")

client = Client()

def start_insta():
    print("📸 جاري تسجيل الدخول إلى إنستقرام...")
    try:
        client.login(USERNAME, PASSWORD)
        print("✅ تم تسجيل دخول سعيد ثون إلى إنستقرام!")
        
        # الحصول على آخر رسالة لمنع الرد على الرسائل القديمة عند التشغيل
        last_checked_time = time.time()

        while True:
            try:
                # جلب الرسائل غير المقروءة
                threads = client.direct_threads()
                for thread in threads:
                    if thread.unread_count > 0:
                        for message in thread.messages:
                            # التأكد أن الرسالة جديدة ولم يتم الرد عليها
                            if message.timestamp.timestamp() > last_checked_time:
                                user_text = message.text
                                user_id = thread.pk
                                
                                # إرسال النص للمعالج المركزي
                                response = handle_logic(user_text)
                                
                                if response:
                                    client.direct_answer(thread.id, response)
                                    print(f"📩 تم الرد على: {user_text}")
                
                last_checked_time = time.time()
                time.sleep(10)  # الانتظار قليلاً لتجنب الحظر (Spam)
            except Exception as e:
                print(f"⚠️ خطأ أثناء جلب الرسائل: {e}")
                time.sleep(30)
                
    except Exception as e:
        print(f"❌ فشل تسجيل الدخول: {e}")

if __name__ == "__main__":
    start_insta()
