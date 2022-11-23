from application_context.app_context import app_context
from helper_files.helper import frame_sentiments
sentiment_pipeline = app_context.sentiment_pipeline


def get_sentiments(data):
    model_output = sentiment_pipeline(data)
    sentiments = frame_sentiments(model_output)
    return sentiments
