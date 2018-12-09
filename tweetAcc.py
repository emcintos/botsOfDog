from twython import Twython
import trainer
import generator

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# twitter.update_status(status="created by @csuitedNerd for a school project, hold for shenanigans")

# print("Tweeteed")

timeline = trainer.get_tweets(twitter)
for tweet in timeline:
    if tweet['truncated'] is False and tweet['is_quote_status'] is False:
        chain = trainer.train_markov(tweet['text'])
    else:
        continue

status = generator.generate_tweet(chain)

twitter.update_status(status=status)
print("Tweeted")
