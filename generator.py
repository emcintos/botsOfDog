import random as r


def generate_tweet(chainmodel):
    tweet = []
    while True:
        if not tweet:
            words = chainmodel['START']
        elif tweet[-1] in chainmodel['END']:
            break
        elif len(tweet) > 25 and tweet[-1] == '.':
            break
        else:
            words = chainmodel[tweet[-1]]
        tweet.append(r.choice(words))
    return " ".join(tweet)