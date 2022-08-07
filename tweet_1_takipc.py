import tweepy
TWITTER_CONSUMER_KEY = 'ZPw9IUsuKUFomxA2ZcVhl9FDD'
TWITTER_CONSUMER_SECRET = 'z46ky2QJzxGOBYVNK7ShqhQewmTEWCFabmLGnReqoxYIbWxgGj'
TWITTER_ACCESS_TOKEN = '83256274-GaBHrEwopd31LYJ5cgtt6XFFvRJNQcafnKfPOXGQB'
TWITTER_ACCESS_TOKEN_SECRET = 'UrldiAOGCBnLnlfZ8rbnbOIOj46ldXifau06NiXb4g2mb'
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
takipciler = tweepy.Cursor(api.followers, id="turkayyildiz965").items(100)
for takipci in takipciler:
    i=i+1
    print(i,takipci.name,takipci.screen_name)
    
