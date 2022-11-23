import requests
from application_context.app_context import app_context
from helper_files.helper import create_list_of_tweets
import time


def get_twitter_data(org):
    base_url = app_context.twitter_search_base_url
    url = str(base_url) + str(org.name)
    headers = app_context.twitter_search_headers
    response = requests.request("GET", url, headers=headers)
    time.sleep(5)
    tweets = create_list_of_tweets(response.text)
    return tweets

