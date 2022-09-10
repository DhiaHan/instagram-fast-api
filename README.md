# How to set up:

## 1. Clone the repository
## 2. pip/pip3 install requests

#Basic using:

```
from instagramFastApi import Client

client = Client()

USERNAME = 'Instagram username'
PASSWORD = 'Instagram password'

cl.login(USERNAME, PASSWORD)
cl.follow(SOMEONE)
cl.unfollow(SOMEONE)
cl.like_post(POST_URL)
cl.unlike_post(POST_URL)

results = cl.search(search_for='Quran')
print(results['users'])
print(results['places'])
print(results['hashtags'])
```

## There's other functions like:

```
cl.change_password(NEW_PASSWORD)

cl.user_id(USERNAME) #Returns user id

cl.logout() #logout of account

cl.message(USERNAME, MESSAGE_TEXT) #Soon

cl.report(USERNAME) #Soon
```
