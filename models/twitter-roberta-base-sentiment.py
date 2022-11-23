from application_context.app_context import app_context
sentiment_pipeline = app_context.sentiment_pipeline


def get_sentiments(data):
    return sentiment_pipeline(data)
