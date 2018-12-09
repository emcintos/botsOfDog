from twython import Twython, TwythonError
# import twython.endpoints as endpoints


def get_tweets(twitter):
    try:
        timeline = twitter.get_user_timeline(screen_name='dog_feelings', exclude_replies=True, include_rts=False)
    except TwythonError as e:
        print(e)
    return timeline


chainmodel = {}


def train_markov(tweet):
    global chainmodel
#     tweet.replace('.', '')
    tweet = tweet.lower().split()
    for i, word in enumerate(tweet):
        if i == len(tweet) - 1:
            chainmodel['END'] = chainmodel.get('END', []) + [word]
        else:
            if i == 0:
                chainmodel['START'] = chainmodel.get('START', []) + [word]
            chainmodel[word] = chainmodel.get(word, []) + [tweet[i+1]]
    return chainmodel
