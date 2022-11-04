from flask import Flask
from transformers import pipeline

app = Flask(__name__)


@app.route('/hello/', methods=['GET'])
def get_sentiments():
    sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
    data = ["i'll buy the iphone x if it can get acCURATE FUCKING WEATHER REPORTS", "Some dude in FB selling the iPhone X 64 gb for $1100 like nigga no one is gonna buy that shit when they can get the 256 gb for that price"]
    return sentiment_pipeline(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)