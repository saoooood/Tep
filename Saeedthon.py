import os, subprocess, base64, shutil, time, random, datetime

# --- 1. العقل المدبر (أوامر سعيد ذبحان) ---
def handle_logic(text):
    if not text: return None
    cmd = text.lower().strip()
    if cmd in [".الذبحاني", ".ذبحان"]:
        return "👑 **الذبحاني**.. أصل الكرم والوفاء، رجال الشدائد ومنبع العز. والنعم بـ سعيد وكل أهل ذبحان."
    elif cmd == ".خدمات":
        return "🚀 **خدمات سعيد ثون للزيادة**\n✅ دعم قنوات تليجرام\n✅ دعم جروبات واتساب\n💬 اطلب عبر: .مطور"
    elif cmd in [".شعر", ".بدوي"]:
        ashar = ["ما يكسر الذبحاني الوقت لو جار.. حنّا جبالٍ ما تهزها العواصف. 🌋", "الذيب ما يهرول عبث.. والرفيق الكفو ذخر الليالي. ✨"]
        return f"📜 **{random.choice(ashar)}**"
    elif cmd == ".فحص":
        return "✅ **سعيد ثون [Saeedthon]** شغال لعيون الذبحاني! 🚀"
    elif cmd == ".الوقت":
        return f"⏰ الوقت في صنعاء: **{datetime.datetime.now().strftime('%I:%M %p')}**"
    elif cmd == ".مطور":
        return "👑 مطور النظام: سعيد حسن الذبحاني\n📍 صنعاء - اليمن"
    return None

# --- 2. محرك الواتساب ---
def run_whatsapp(env):
    try:
        from neonize.client import NewClient
        def on_msg(client, message):
            try:
                text = message.Message.conversation or message.Message.extendedTextMessage.text
                res = handle_logic(text)
                if res: client.send_message(message.Info.RemoteJid, res)
            except: pass
        
        wa_session = os.getenv("WA_SESSION")
        if wa_session:
            with open("session.db", "wb") as f: f.write(base64.b64decode(wa_session))
            client = NewClient("session.db")
            client.add_event_handler(on_msg)
            client.connect()
    except Exception as e: print(f"❌ واتساب متوقف: {e}")

# --- 3. تشغيل النظام ---
def start_engine():
    print("🚀 [سعيد ثون] جاري التشغيل بدون إنستقرام...")
    
    repo = base64.b64decode("aHR0cHM6Ly9naXRodWIuY29tL21kYWgyNTE5LWJ5dGUvUmU=").decode()
    if os.path.exists("source_temp"): shutil.rmtree("source_temp")
    subprocess.run(f"git clone {repo} source_temp", shell=True)
    os.chdir("source_temp")
    
    # تثبيت المكاتب الضرورية فقط
    subprocess.run("pip install telethon neonize-python Flask gunicorn requests", shell=True)
    
    env = os.environ.copy()
    env["DATABASE_URL"] = os.getenv("DATABASE_URL", "sqlite:///saeed.db")
    env["STRING_SESSION"] = os.getenv("TG_SESSION", "")
    
    # تشغيل ت
