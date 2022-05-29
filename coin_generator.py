cid ="101974055"

#from keep_alive import keep_alive
import os
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
    import colorama
try:
    import pyfiglet
except ModuleNotFoundError:
    os.system("pip install pyfiglet")
    import pyfiglet
from colorama import init, Fore, Back, Style
print("\n\n\33[48;5;5m\33[38;5;234m ❮ COIN GENERATOR❯ \33[0m\33[48;5;235m\33[38;5;5m \33[0m")

import aminofix as amino
from uuid import uuid4
import requests
import threading
import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from os import path
import json
THIS_FOLDER = path.dirname(path.abspath(__file__))
emailfile=path.join(THIS_FOLDER,"accounts.json")
dictlist=[]

with open(emailfile) as f:
    dictlist = json.load(f)

def magicnum():
    toime={"start":int(datetime.timestamp(datetime.now())),"end":int(datetime.timestamp(datetime.now()))+300}
    return toime

def sendobj(sub : amino.SubClient):
    timer=[
    magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum()
    ]
    sub.send_active_obj(timers=timer)

def log(cli : amino.Client,email : str, password : str):
    try:
        cli.login(email=email,password=password)
        print(f"logged into {email}\n")
    except Exception as e:
        print(e)
        pass

def task(sub : amino.SubClient,email : str,i : int):
    try:
        sendobj(sub)
        print(f"Generated Coins for {email} times :- {i+1}")
    except:
        return None

def threadit(acc : dict):
    email=acc["email"]
    device=acc["device"]
    password=acc["password"]
    client=amino.Client(deviceId=device)
    log(cli=client,email=email,password=password)
    client.join_community(cid)
    subclient=amino.SubClient(comId=cid,profile=client.profile)
    for i in range(25):
    	time.sleep(5)
    	try:
    		task(subclient,email,i)
    	except:
    		pass
   # client.logout()
    print(f"Generated Coins with {email}")
def main():
    print(f"\n\33[93;5;5m\33[93;5;234m ❮ Total Accounts : {len(dictlist)} ❯ \33[0m\33[93;5;235m\33[93;5;5m \33[0m")
    for amp in dictlist:
    	threadit(amp)
    print(f'Claimed coins from {len(dictlist)} accounts')
 
if __name__ == '__main__':
	main()