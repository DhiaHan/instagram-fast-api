import requests
from Constants import headers, data, URL, LOGIN_URL
from datetime import datetime

class Client():
    def __init__(self, proxy=None, headers_file=None):
        self.proxy = proxy
        self.session = requests.session()        
        self.headers = headers
        self.session.headers = self.headers
        self.data = data
        self.url = URL
        self.login_url = LOGIN_URL
        self.selfId: str
        self.logged_in = False

    def __enc_password(self, passwd):
        return '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(datetime.now().timestamp()), passwd)

    def __get_cookies(self, update=True):
        
        toret = []
        cookies = self.session.get(self.url, proxies=self.proxy).cookies
        csrftoken = cookies['csrftoken']
        toret.append(csrftoken)
        try:toret.append(cookies['ig_did'])
        except:pass
        try:toret.append(cookies['ig_nrcb'])
        except:pass
        try: toret.append(cookies['mid'])
        except:pass
        if update:
            self.session.headers.update({"X-CSRFToken":csrftoken})
        if len(toret) == 1 or len(toret) == 4 : return toret

    def login(self, user, passw):
        self.user, self.passw = user, passw
        self.session = requests.session()
        self.session.headers = self.headers
        self.__get_cookies()
        self.data.update({'username':user})
        self.data.update({'enc_password':self.__enc_password(passw)})
        resp = self.session.post(self.login_url,
                                    data=self.data, proxies=self.proxy)
        
        self.session.headers.update({'X-CSRFToken':resp.cookies['csrftoken']})
        self.selfId = resp.json()['userId']
        self.logged_in = True
        return resp

    def logout(self):
        url = 'https://i.instagram.com/api/v1/web/accounts/logout/ajax/'
        resp = self.session.post(url, data={"one_tap_app_login":"0", "user_id":self.selfId})
        return resp
        
    def user_id(self, user):
        url = 'https://www.instagram.com/web/search/topsearch/?query='+user
        data = self.session.get(url, proxies=self.proxy).json()
        return data['users'][0]['user']['pk']

    def report(self, username): pass #TODO

    def __funf(self, username, endpoint):
        user_id = self.user_id(username)
        url = f'https://i.instagram.com/api/v1/web/friendships/{user_id}/{endpoint}/'
        return self.session.post(url, data='')
        
    def follow(self, username) : return self.__funf(username, 'follow')
    
    def unfollow(self, username) : return self.__funf(username, 'unfollow')

    def change_password(self, new_passw):
        url = 'https://www.instagram.com/accounts/password/change/'
        data = {
            'enc_old_password':self.__enc_password(self.passw),
            'enc_new_password1':self.__enc_password(new_passw),
            'enc_new_password2':self.__enc_password(new_passw),
        }
        resp = self.session.post(url, data=data)
        if int(resp.status_code) == 200 : self.passw = new_passw
        return resp

    def set_gender(self, gender: str):
        if gender.lower() not in ['male', 'female', 'm', 'f']:
            print('?')
            exit()
        url = 'https://i.instagram.com/api/v1/web/accounts/set_gender/'
        data = {'gender':gender, 'custom_gender':''}
        return self.session.post(url, data=data)

    def is_real(self, username):
        url = 'https://i.instagram.com/api/v1/users/check_username/'
        return not self.session.post(url, data={'username':username}).json()['available']

    def __org_search_res(self, users, places, hashs, show_first):
        usernames = [i['user']['username'] for i in users]
        hashtags = [i['hashtag']['name'] for i in hashs]
        places = [i['place']['location']['name'] for i in places]
        if show_first != None:
            usernames = usernames[:show_first]
            hashtags = hashtags[:show_first]
            places = places[:show_first]
        return {
            'users': usernames,
            'hashtags': hashtags,
            'places': places 
        }

    def search(self, search_for, show_first=None):
        url = 'https://i.instagram.com/api/v1/web/search/topsearch/?context=blended&query='
        url = url + search_for
        response = self.session.get(url).json()
        users = response['users']
        places = response['places']
        hashtags = response['hashtags']
        return self.__org_search_res(*[users, places, hashtags], show_first)  
       
    def __like_post_with_id(self, post_id, action):
        url = 'https://www.instagram.com/web/likes/{}/{}/'.format(post_id, action)
        return self.session.post(url, data='')
    
    def __post_url2id(self, url):
        r = self.session.get(url)
        placement_str = 'instagram://media?id='
        p = r.text.find(placement_str)
        raw_id = r.text[p:p+100]
        post_id = raw_id.split('"')[0].split('=')[1]
        return post_id
    
    def __lunl(self, url, action):
        self.__like_post_with_id(self.__post_url2id(url), action)
    
    def like_post(self, post_url):
        return self.__lunl(post_url, 'like')
    
    def unlike_post(self, post_url):
        return self.__lunl(post_url, 'unlike')

    def message(self, username, text): pass #TODO
