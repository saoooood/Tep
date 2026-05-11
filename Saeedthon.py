import os
import subprocess
import base64
import shutil

# الرابط المشفر لسورس التشغيل الأساسي
repo_encoded = "aHR0cHM6Ly9naXRodWIuY29tL21kYWgyNTE5LWJ5dGUvUmU="
branch = "main"

def run(cmd):
    print(f"⌭ تنفيذ: {cmd}")
    return subprocess.Popen(cmd, shell=True)

def _run_git_clone():
    print("• جـاري تحميل سورس سعيد ثون [Saeedthon].....")
    try:
        repo_url = base64.b64decode(repo_encoded.replace(" ", "")).decode()
        if not os.path.exists("source_temp"):
            subprocess.run(f"git clone -b {branch} {repo_url} source_temp", shell=True, check=True)
        
        # نقل ملفاتك البرمجية من المجلد الرئيسي إلى داخل مجلد السورس لكي تعمل معاً
        files_to_move = ["processor.py", "insta_bot.py", "whatsapp_bot.py"]
        for file in files_to_move:
            if os.path.exists(f"../{file}"):
                shutil.copy(f"../{file}", f"./source_temp/{file}")
            elif os.path.exists(file): # في حال كان الملف في نفس المستوى
                shutil.copy(file, f"./source_temp/{file}")
                
        os.chdir("source_temp")
    except Exception as e:
        print(f"❌ خطأ في التحميل أو نقل الملفات: {e}")

def _install_requirements():
    print("⌭ تثبيت مكاتب سعيد ثون الشاملة ⌭")
    # أضفنا مكتبة neonize-bin للواتساب
    subprocess.run("pip install -r requirements.txt instagrapi neonize-bin Flask", shell=True, check=True)

def _start_project():
    print("⌭ البدء بتشغيل نظام سعيد ثون للمنصات المتعددة ⌭")
    
    procs = []
    
    # 1. تشغيل سيرفر الحماية
    procs.append(run("python3 server.py"))
    
    # 2. تشغيل بوت التيليجرام
    print("🚀 تشغيل سعيد ثون على تيليجرام...")
    procs.append(run("python3 -m Tepthon")) 
    
    # 3. تشغيل بوت الإنستقرام
    if os.path.exists("insta_bot.py"):
        print("📸 تشغيل سعيد ثون على إنستقرام...")
        procs.append(run("python3 insta_bot.py"))
        
    # 4. تشغيل بوت الواتساب
    if os.path.exists("whatsapp_bot.py"):
        print("🟢 تشغيل سعيد ثون على واتساب...")
        procs.append(run("python3 whatsapp_bot.py"))

    print("\n✅ سعيد ثون انطلق الآن!")
    
    # الحفاظ على السكريبت يعمل للأبد (عشان GitHub Action ما يقفل)
    for p in procs:
        p.wait()

if __name__ == "__main__":
    _run_git_clone()
    _install_requirements()
    _start_project()
