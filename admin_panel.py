#!/usr/bin/env python3
# Admin Panel for Sk Parvez SMS Bomber

import json
import os
from datetime import datetime

TELEGRAM_BOT_TOKEN = "8344986767:AAGyVe8mGIQ1FspNAKUdL_Tqz9YXPbV0aLw"
ADMIN_ID = "8293984966"

def show_admin_panel():
    print("""
╔══════════════════════════════════════╗
║        SK PARVEZ ADMIN PANEL         ║
╚══════════════════════════════════════╝
""")
    
    if os.path.exists("attack_logs.json"):
        with open("attack_logs.json", "r") as f:
            logs = json.load(f)
        
        print(f"📊 Total Attacks: {len(logs)}\n")
        
        for log in reversed(logs):
            print(f"📱 {log['phone']}")
            print(f"   📤 SMS: {log['sms_sent']}")
            print(f"   ✅ Rate: {log['success_rate']:.1f}%")
            print(f"   ⏱️ Time: {log['time']}")
            print(f"   👤 User: {log.get('user_ip', 'N/A')}")
            print()
    else:
        print("No attack logs found.")

if __name__ == "__main__":
    show_admin_panel()