from API.instagram_private_api import Client
import time
import random
from Bots.Functions.API import login

api = login.login()

pending = api.friendships_pending()

total = 0
while pending["users"]:
    for user in pending["users"]:
        randtime=random.randint(1,10)
        randtime=randtime/10
        api.approve(user["pk"])
        total+=1
        print("Accepted:", total, end="\n", flush=True)
        time.sleep(randtime/100)
    pending = api.friendships_pending()
print("Accepted:", total, end='\r', flush=True)