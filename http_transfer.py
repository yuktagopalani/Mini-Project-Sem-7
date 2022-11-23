import requests
from application_context.app_context import app_context


def get_twitter_data(org):
    base_url = app_context.twitter_search_base_url
    url = base_url + org.name
    headers = app_context.twitter_search_headers
    response = requests.request("GET", url, headers=headers)
    return response.text

