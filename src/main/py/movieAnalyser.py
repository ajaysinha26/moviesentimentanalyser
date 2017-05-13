import sys
import tweepy
from textblob import TextBlob

consumer_key = sys.argv[1]
consumer_secret = sys.argv[2]

access_token = sys.argv[3]
access_token_secret = sys.argv[4]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

movie = sys.argv[5]
public_tweets = api.search(q=movie, count=100)
verdict = 0
count = 0
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    verdict += analysis.sentiment.polarity
    count += 1

print('***Sentiment of movie is: ', verdict)
print('***No. of tweets analysed: ', count)