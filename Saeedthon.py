import os
import subprocess
import base64

# الرابط المشفر لسورس التشغيل الأساسي
repo_encoded = "aHR0cHM6Ly9naXRodWIuY29tL21kYWgyNTE5LWJ5dGUvUmU="
branch = "main"

def run(cmd):
    print(f"⌭ تنفيذ: {cmd}")
    # استخدام Popen للسماح بتشغيل عدة بوتات في نفس الوقت
    return subprocess.Popen(cmd, shell=True)

def _run_git_clone():
    print("• جـاري تحميل سورس سعيد ثون [Saeedthon].....")
    try:
        repo_url = base64.b64decode(repo_encoded.replace(" ", "")).decode()
        if not os.path.exists("source_temp"):
            subprocess.run(f"git clone -b {branch} {repo_url} source_temp", shell=True, check=True)
        os.chdir("source_temp")
    except Exception as e:
        print(f"❌ خطأ في التحميل: {e}")

def _install_requirements():
    print("⌭ تثبيت مكاتب سعيد ثون (تيليجرام + انستا + واتساب) ⌭")
    # تثبيت المتطلبات الأساسية بالإضافة لمكتبة الانستجرام
    subprocess.run("pip install -r requirements.txt instagrapi", shell=True, check=True)

def _start_project():
    print("⌭ البدء بتشغيل نظام سعيد ثون للمنصات المتعددة ⌭")
    
    # 1. تشغيل سيرفر الحماية (Server) في الخلفية
    run("python3 server.py")
    
    # 2. تشغيل بوت التيليجرام الأساسي (سعيد ثون)
    print("🚀 تشغيل سعيد ثون على تيليجرام...")
    run("python3 -m Tepthon") 
    
    # 3. تشغيل بوت الإنستقرام
    if os.path.exists("insta_bot.py"):
        print("📸 تشغيل سعيد ثون على إنستقرام...")
        run("python3 insta_bot.py")
        
    # 4. تشغيل بوت الواتساب
    if os.path.exists("whatsapp_bot.py"):
        print("🟢 تشغيل سعيد ثون على واتساب...")
        run("python3 whatsapp_bot.py")

    print("\n✅ نظام سعيد ثون يعمل الآن على كافة المنصات المتوفرة.")
    print("يمكنك متابعة السجلات (Logs) من لوحة تحكم GitHub أو Render.")
    
    # الحفاظ على العملية نشطة
    try:
        # الانتظار لمنع توقف السكريبت الأساسي
        subprocess.wait() 
    except:
        pass

if __name__ == "__main__":
    _run_git_clone()
    _install_requirements()
    _start_project()
