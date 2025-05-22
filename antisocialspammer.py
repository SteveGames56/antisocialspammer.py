import string, json, requests, random
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep

system('cls')
sent_count = 0


avatars = [
    "https://cdn.discordapp.com/icons/1297491094791262249/a_c7e0b28459b8260f7649f5a58210f2c9.gif?size=1024&width=509&height=509",
]
              Coded by SteveGames ❤️
"""

def send_message(webhook_url, message):
    global sent_count
    username = "antisocial on top"
    avatar = "https://cdn.discordapp.com/icons/1297491094791262249/a_c7e0b28459b8260f7649f5a58210f2c9.gif?size=1024&width=509&height=509"

    data = json.dumps({
        "content": message,
        "username": username,
        "avatar_url": avatar,
        "tts": False
    })

    headers = {
        "content-type": "application/json"
    }

    try:
        response = requests.post(webhook_url, data=data, headers=headers)
        if response.status_code == 204:
            sent_count += 1
            print(Colorate.Horizontal(Colors.purple_to_blue, f"[✓] Message sent! Total: {sent_count}"))
        elif response.status_code == 429:
            print(Colorate.Horizontal(Colors.red_to_yellow, "[!] Rate limited! Waiting 2 seconds..."))
            sleep(2)  
        else:
            print(Colorate.Horizontal(Colors.red_to_black, f"[✗] Failed with status code: {response.status_code}"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_black, f"[!] Error: {e}"))


while True:
    system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(header_final)))
    print(Colorate.Horizontal(Colors.purple_to_blue, "[-] Webhook URL ↓"))
    webhook_url = input(">>> ").strip()
    if webhook_url.startswith("https://discord.com/api/webhooks/"):
        break
    else:
        print(Colorate.Horizontal(Colors.red_to_black, "[!] Invalid webhook URL!"))
        sleep(2)

system('cls')
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(header_final)))
print(Colorate.Horizontal(Colors.purple_to_blue, "[+] Enter the message to send:"))
message_to_send = input(">>> ").strip()


while True:
    send_message(webhook_url, message_to_send)
