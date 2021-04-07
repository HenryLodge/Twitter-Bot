import tweepy
import time

auth = tweepy.OAuthHandler('--api key here--', '--secret api key here--')
auth.set_access_token('--access token here--', '--secret access token here--')

api = tweepy.API(auth)
user = api.me()

def limit_handle(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(1000)


# public_tweets = tweepy.Cursor(api.home_timeline()).items(200)
for tweet in tweepy.Cursor(api.home_timeline).items(200):
    try:
    	limit_handle(tweet.favorite())
    except tweepy.TweepError as e:
    	error = True
    	print(e.reason)
