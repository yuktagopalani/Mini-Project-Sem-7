from dataclasses import dataclass

import transformers
from transformers import pipeline


@dataclass
class AppContext:
    sentiment_pipeline: transformers.pipelines
    twitter_search_base_url: str
    twitter_search_headers: dict

    def __init__(self):
        self.sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
        self.twitter_search_base_url = "https://api.twitter.com/2/tweets/search/recent?query="
        self.twitter_search_headers = {
            'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAKOwiwEAAAAAtKyB0zMcFq0Qpz%2FFgPmbLbE1c9E%3DgW25ZZjYQladyqKCAzRassZLVZvvG7PvHiPhiKVvyo4oAhmDzj',
            'Cookie': 'guest_id=v1%3A166341311025469413'
        }


app_context = AppContext()
