import json
from flask import Flask, request
from application_context.app_context import app_context
import requests

app = Flask(__name__)



# def get_twitter_data():
#     url = "https://api.twitter.com/2/tweets/search/recent?query="
#
#     payload = {}
#     headers = {
#         'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAKOwiwEAAAAAnMlPApzvBJT4tvPZM%2BFDWwl%2F3ME%3DXKbifYqcL6LGv0SkipQZwevhgP6YTsFIKhUfdzkSbCyOxr1isc',
#         'Cookie': 'guest_id=v1%3A166341311025469413'
#     }
#
#     response = requests.request("GET", url, headers=headers, data=payload)
#     return response.text


@app.route('/sentiments/', methods=['GET'])
def convert_json_to_list():
    twitter_data = json.loads(get_twitter_data())
    data = []
    for item in twitter_data['data']:
        data.append(item['text'])

    # input_json = request.get_json()
    # data = input_json['data']
    return get_sentiments(data)







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
