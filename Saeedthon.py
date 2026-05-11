import os
import subprocess
import base64
import time

repo_encoded = "aHR0cHM6Ly9naXRodWIuY29tL21kYWgyNTE5LWJ5dGUvUmU="
branch = "main"

def run(cmd):
    return subprocess.Popen(cmd, shell=True)

def _setup():
    print("🚀 جاري تجهيز نظام سعيد ثون...")
    repo_url = base64.b64decode(repo_encoded).decode()
    if not os.path.exists("source_temp"):
        subprocess.run(f"git clone -b {branch} {repo_url} source_temp", shell=True)
    
    tg_session = os.getenv("TG_SESSION")
    if tg_session:
        with open("source_temp/saeed.session", "wb") as f:
            f.write(base64.b64decode(tg_session))
            
    os.chdir("source_temp")
    # تحميل المكتبات المطلوبة
    subprocess.run("pip install -r requirements.txt instagrapi neonize-bin Flask", shell=True)

def _start():
    print("🔥 تشغيل المنصات بشكل آمن (تليجرام، انستا، واتساب)...")
    run("python3 server.py")
    run("python3 -m Tepthon") 
    run("python3 ../insta_bot.py")
    run("python3 ../whatsapp_bot.py")
    
    print("✅ سعيد ثون يعمل الآن بالبيانات المخفية")
    while True: time.sleep(100)

if __name__ == "__main__":
    _setup()
    _start()
