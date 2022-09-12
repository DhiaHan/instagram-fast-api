# How to set up:

## 1. Clone the repository
## 2. pip/pip3 install requests

#Basic using:

```
from instagramFastApi import Client

client = Client()

USERNAME = 'Instagram username'
PASSWORD = 'Instagram password'

client.login(USERNAME, PASSWORD)
client.follow(SOMEONE)
client.unfollow(SOMEONE)
client.like_post(POST_URL)
client.unlike_post(POST_URL)

results = client.search(search_for='Quran')
print(results['users'])
print(results['places'])
print(results['hashtags'])
```

## There's other functions like:

```
client.change_password(NEW_PASSWORD)

client.user_id(USERNAME) #Returns user id

client.set_gender(gender='male') #change account's gender

client.logout() #logout of account

client.message(USERNAME, MESSAGE_TEXT) #Soon

client.report(USERNAME) #Soon
```
