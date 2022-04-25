import feedparser
import random
import re

def get_tweets():

    # get last tweets from twitter bot
    feed = feedparser.parse('https://nitter.net/ntsweirdo/rss')

    # extract the tweets
    tweets = [m['title'] for m in feed.entries]

    return tweets

def sanitize_tweet(tweet):

    # @TODO restrict gif links to three times posted
    gif_links = re.finditer(r'http[s]?://[^\s]*[gif|giph|webm][^\s]*', tweet, flags=re.IGNORECASE)
    gif_links = [m for m in gif_links]

    if len(gif_links) > 3:
        for i, link in enumerate(gif_links):
            if i > 2:
                # replace occurence of link in tweet
                tweet[link.start():link.end()] = ''

    # remove . before @
    tweet = re.sub(r'\.(@[^\s]*)', r'\1', tweet)

    return tweet


def get_random_tweet():

    tweets = get_tweets()

    random_tweet = random.choice(tweets)

    # sanitize tweet
    random_tweet = sanitize_tweet(random_tweet)

    return random_tweet