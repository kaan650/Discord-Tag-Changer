import requests
import time
import json

config_data = json.loads(open("config.json", "r").read())
newSession = requests.Session()
headers = {
    'Authorization': config_data["token"],
    'Content-Type': 'application/json',
}

def getTag():
    response = newSession.get(config_data["discordLink"], headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        return str(user_data['discriminator'])
    else:
        print(f"Error on getting user tag {response.status_code}: {response.reason}")

def changeUsername():
    data = {
        "username": getTag(),
        "password": config_data["password"]
    }
    response = newSession.patch(config_data["discordLink"], json=data, headers=headers)
    if response.status_code == 200:
        print("Successfull!")
    else:
        print(f"Error on changing username {response.status_code}: {response.text}")

def init(seconds):
    while True:
        changeUsername()
        time.sleep(seconds)

init(config_data["cooldown"])
