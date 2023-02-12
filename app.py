from flask import Flask, render_template, url_for, request
import boto3
import json

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    input_text = "これまでに訪れたことがない本当にクールな新しい場所を見つけたいと考えていましたが、ここにはそのような情報はありませんでした。お勧めのいくつかはひどいのもので、笑うしかありませんでした。 ほとんどのお勧めは、一般的な大都市やレストラン、バーなどでした。よく知られた情報ばかりでした。掲載されている場所に行って楽しみたいとは思いません。この本を購入する価値はまったくありません。"
    return render_template('index.html', text_input = input_text)

@app.route('/', methods=['POST'])
def form():
    input_text = request.form['input_text']

    comprehend = boto3.client(
        service_name = 'comprehend',
        region_name = 'ap-northeast-1',
        aws_access_key_id = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        aws_secret_access_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    )
    result = comprehend.detect_sentiment(Text = input_text, LanguageCode = 'ja' )
    
    print(result["Sentiment"])

    #for k, v in result["SentimentScore"].items():
    #    print(f"    {k}:  {v}")

    return render_template('index.html', \
        text_input = input_text, \
        text_json = result, \
        sentiment = result["Sentiment"]
    )

if __name__ == '__main__':
   app.run()
