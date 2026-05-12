import os
import subprocess
import base64
import shutil

# رابط السورس المشفر
repo_url = base64.b64decode("aHR0cHM6Ly9naXRodWIuY29tL21kYWgyNTE5LWJ5dGUvUmU=").decode()

def _fix_and_run():
    print("🚀 جاري معالجة النظام لعيون الذبحاني...")
    if os.path.exists("source_temp"): shutil.rmtree("source_temp")
    subprocess.run(f"git clone {repo_url} source_temp", shell=True)
    
    os.chdir("source_temp")
    
    # حل مشكلة neonize-bin وتثبيت المكاتب الصحيحة
    print("📦 جاري تثبيت المكاتب...")
    subprocess.run("pip install telethon instagrapi neonize-python Flask gunicorn requests heroku3", shell=True)
    
    # إعداد البيئة لتجاوز خطأ NoneType المزعج
    env = os.environ.copy()
    env["DATABASE_URL"] = os.getenv("DATABASE_URL", "sqlite:///saeed.db")
    env["API_ID"] = os.getenv("API_ID", "")
    env["API_HASH"] = os.getenv("API_HASH", "")
    env["STRING_SESSION"] = os.getenv("TG_SESSION", "")
    
    # تشغيل البوتات في الخلفية
    print("🔥 سعيد ثون ينطلق الآن!")
    subprocess.Popen("python3 -m Tepthon", shell=True, env=env)
    
    # تشغيل الواتساب إذا وجد ملفه
    if os.path.exists("../whatsapp_bot.py"):
        shutil.copy("../whatsapp_bot.py", "./")
        subprocess.Popen("python3 whatsapp_bot.py", shell=True, env=env)
    
    # الحفاظ على الجلسة حية
    while True: 
        import time
        time.sleep(100)

if __name__ == "__main__":
    _fix_and_run()
