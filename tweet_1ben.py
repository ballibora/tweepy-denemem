import tweepy
#boşluklar kişiye özel tanımlanmalı
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

ben=api.me()
#print(ben)

print(ben.id)
print(ben.screen_name)
print(ben.name)
print(ben.description)
print(ben.created_at)
print(ben.followers_count)
print(ben.friends_count)




