import requests


def get_twitter_data(org):
    url = "http://localhost:8000/critical_tweets/"
    input_json = {
        "organisation": org
    }
    response = requests.request("POST", url, json=input_json)
    return response.text
