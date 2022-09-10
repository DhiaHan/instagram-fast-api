import random

with open('user_agents.txt', 'r') as f:
	s = f.read().strip().split('\n')

def random_agent():
    return random.choice(s)

URL = 'https://www.instagram.com/'
LOGIN_URL = URL + 'accounts/login/ajax/'
headers = {
    "User-Agent": random_agent(),
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "X-CSRFToken": "",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.instagram.com/",
    "Content-Type":"application/x-www-form-urlencoded"
		}

data = {
    "enc_password":"",
    "username":"",
    "queryParams":"{}",
    "optIntoOneTap":"false",
    "stopDeletionNonce":"",
    "trustedDeviceRecords":"{}"
	}
	
