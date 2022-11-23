from structures.tweet import Tweet

from structures.organisation import Organisation

from structures.sentiment import Sentiment
from flask import jsonify
import ast


def create_list_of_tweets(response):
    tweets = []
    twitter_data = ast.literal_eval(response)

    for item in twitter_data['data']:
        tweet_id = item['id']
        tweet_text = item['text']
        tweet = Tweet(tweet_id, tweet_text)
        tweets.append(tweet)
    return tweets


def frame_json_to_object(input_json):
    org = Organisation(input_json['organisation'])
    return org


def create_list_of_tweet_texts(tweets):
    tweet_texts = []
    for tweet in tweets:
        tweet_texts.append(tweet.text)
    return tweet_texts


def frame_sentiments(model_output):
    sentiments = []
    for item in model_output:
        label = 'positive'
        polarity = item['score']
        if item['label'] == 'LABEL_0':
            label = 'negative'
        elif item['label'] == 'LABEL_1':
            label = 'neutral'
        sentiment = Sentiment(label, polarity)
        sentiments.append(sentiment)

    return sentiments


def frame_output_json(tweets, sentiments):
    data = []
    number_of_tweets = len(tweets)
    for i in range(number_of_tweets):
        if sentiments[i].label == 'negative':
            information = {
                'tweet_id': tweets[i].id,
                'tweet_text': tweets[i].text,
                'sentiment': {
                    'label': sentiments[i].label,
                    'polarity': sentiments[i].polarity
                },
                'tweet_url': "https://twitter.com/i/web/status/" + tweets[i].id
            }
            data.append(information)
    return jsonify(data)

