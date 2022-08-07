import tweepy
#boş bırakılan yerler kişiye özel olarak tanımlanır
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

"""
#yöntem1
takipciler = api.followers (id="mubbud", count=100)
i=0
for takipci in takipciler:
    
    i=i+1
    print(i,"-",takipci.name,"(",takipci.screen_name,")",takipci.description)
"""

#yöntem2
i=0
takipciler = tweepy.Cursor(api.followers, id="").items(100) #idye takipçilerini öğrenmek istediğiniz kullanıcının kullanıcı adını girmeniz gerekir
for takipci in takipciler:
    i=i+1
    print(i,takipci.name,takipci.screen_name)
    
