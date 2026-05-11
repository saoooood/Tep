import os
import subprocess
import base64
import time
import shutil

# رابط السورس الأساسي (Tepthon)
repo_encoded = "aHR0cHM6Ly9naXRodWIuY29tL21kYWgyNTE5LWJ5dGUvUmU="
branch = "main"

def run_proc(cmd, env=None):
    print(f"⌭ جاري تشغيل: {cmd}")
    return subprocess.Popen(cmd, shell=True, env=env)

def _setup_environment():
    print("🚀 [سعيد ثون] جاري تحضير المحركات وتجهيز البيئة...")
    
    # 1. فك تشفير الرابط وتحميل السورس
    repo_url = base64.b64decode(repo_encoded).decode()
    if os.path.exists("source_temp"): 
        shutil.rmtree("source_temp")
    
    subprocess.run(f"git clone -b {branch} {repo_url} source_temp", shell=True)
    
    # 2. استعادة ملفات البوتات الإضافية والمعالج
    my_files = ["processor.py", "insta_bot.py", "whatsapp_bot.py"]
    for file in my_files:
        if os.path.exists(file): 
            shutil.copy(file, f"source_temp/{file}")
            print(f"✅ تم دمج {file}")

    os.chdir("source_temp")
    
    # 3. تثبيت المكاتب الضرورية (تم إضافة المكتبات الناقصة)
    print("📦 جاري تثبيت المكاتب (قد يستغرق ذلك دقيقة)...")
    subprocess.run("pip install telethon instagrapi neonize-python Flask gunicorn heroku3 requests", shell=True)

def _start_saeedthon():
    print("\n🔥 [سعيد ثون] ينطلق الآن بأقصى طاقة 🔥")
    
    # إعداد بيئة العمل وتمرير الأسرار (Secrets)
    custom_env = os.environ.copy()
    
    # تمرير قاعدة البيانات والتوكن والستيشن
    custom_env["DATABASE_URL"] = "sqlite:///saeed.db"
    custom_env["BOT_TOKEN"] = os.getenv("BOT_TOKEN", "")
    
    # تمرير الستيشن كمتغير نصي (أسرع وأضمن في السحابة)
    tg_session = os.getenv("TG_SESSION", "")
    custom_env["STRING_SESSION"] = tg_session
    custom_env["SESSION"] = tg_session # لضمان التوافق مع بعض النسخ
    
    procs = []
    
    # تشغيل السيرفر (للحماية من الإغلاق)
    procs.append(run_proc("python3 server.py", env=custom_env))
    
    # تشغيل المحرك الأساسي (تليجرام)
    procs.append(run_proc("python3 -m Tepthon", env=custom_env))
    
    # تشغيل إنستقرام إذا وجد ملفه
    if os.path.exists("insta_bot.py"):
        procs.append(run_proc("python3 insta_bot.py", env=custom_env))
        
    # تشغيل واتساب إذا وجد ملفه
    if os.path.exists("whatsapp_bot.py"):
        procs.append(run_proc("python3 whatsapp_bot.py", env=custom_env))

    print("\n✅ سعيد ثون متصل وشغال.. راقب حساباتك يا بطل!")
    
    # الحفاظ على تشغيل العمليات
    for p in procs:
        p.wait()

if __name__ == "__main__":
    try:
        _setup_environment()
        _start_saeedthon()
    except Exception as e:
        print(f"❌ حدث خطأ أثناء التشغيل: {e}")
