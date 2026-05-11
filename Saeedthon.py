import os
import subprocess
import base64
import time
import shutil

repo_encoded = "aHR0cHM6Ly9naXRodWIuY29tL21kYWgyNTE5LWJ5dGUvUmU="
branch = "main"

def run_proc(cmd, env=None):
    print(f"⌭ جاري تشغيل: {cmd}")
    return subprocess.Popen(cmd, shell=True, env=env)

def _setup_environment():
    print("🚀 تجهيز المحركات لعيون الذبحاني...")
    repo_url = base64.b64decode(repo_encoded).decode()
    if os.path.exists("source_temp"): shutil.rmtree("source_temp")
    subprocess.run(f"git clone -b {branch} {repo_url} source_temp", shell=True)
    
    tg_session = os.getenv("TG_SESSION")
    if tg_session:
        with open("source_temp/saeed.session", "wb") as f:
            f.write(base64.b64decode(tg_session))

    my_files = ["processor.py", "insta_bot.py", "whatsapp_bot.py"]
    for file in my_files:
        if os.path.exists(file): shutil.copy(file, f"source_temp/{file}")

    os.chdir("source_temp")
    # تم تصحيح المكاتب هنا لتعمل مع جيت هاب
    subprocess.run("pip install telethon instagrapi neonize-python Flask gunicorn heroku3", shell=True)

def _start_saeedthon():
    print("\n🔥 انطلاق سعيد ثون 🔥")
    
    # حل مشكلة التيليجرام: إضافة قاعدة بيانات وهمية (Sqlite) لكي لا ينهار البوت
    custom_env = os.environ.copy()
    custom_env["DATABASE_URL"] = "sqlite:///saeed.db"
    
    procs = []
    procs.append(run_proc("python3 server.py", env=custom_env))
    procs.append(run_proc("python3 -m Tepthon", env=custom_env))
    
    if os.path.exists("insta_bot.py"):
        procs.append(run_proc("python3 insta_bot.py", env=custom_env))
    if os.path.exists("whatsapp_bot.py"):
        procs.append(run_proc("python3 whatsapp_bot.py", env=custom_env))

    for p in procs: p.wait()

if __name__ == "__main__":
    _setup_environment()
    _start_saeedthon()
