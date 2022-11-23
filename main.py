from flask import Flask, request
from helper_files.helper import frame_json_to_object, frame_output_json, create_list_of_tweet_texts
from helper_files.http_transfer import get_twitter_data
from models.twitter_roberta_base_sentiment import get_sentiments
app = Flask(__name__)


@app.route('/critical_tweets/', methods=['POST'])
def get_response():
    request_data = request.get_json()
    org = frame_json_to_object(request_data)
    tweets = get_twitter_data(org)
    tweet_texts = create_list_of_tweet_texts(tweets)
    sentiments = get_sentiments(tweet_texts)
    response = frame_output_json(tweets, sentiments)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
