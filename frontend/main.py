import streamlit as st
import ast
import pandas as pd

from http_transfer import get_twitter_data


def load_data(org):
    response = get_twitter_data(org)
    twitter_data = ast.literal_eval(response)
    tweet_text = []
    tweet_id = []
    tweet_url = []
    for item in twitter_data:
        tweet_text.append(item['tweet_text'])
        tweet_id.append(item['tweet_id'])
        tweet_url.append(item['tweet_url'])
    return pd.DataFrame(
        {
            "Tweet Text": tweet_text,
            "Tweet ID": tweet_id
            # "Tweet URL": tweet_url
        }
    )


# st.set_page_config(layout="wide")
st.header('Social Media Monitoring')
# org = st.text_input('Enter the organisation/people', 'Elon Musk')
form = st.form(key='my-form')
org = form.text_input('Enter organisation/people')
submit = form.form_submit_button('search')


if submit:
    df = load_data(org)
    st.write(" Critical Tweets are : ")
    st.dataframe(df)

