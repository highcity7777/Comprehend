# Amazon Comprehend 使用のサンプル

## アクセスキーの設定
app.py中のaws_access_key_idとaws_secret_access_keyの値を設定すること

## 仮想環境の作成
1.py -m venv myenv
2.myenv\Scripts\activate
3.Flask,boto3のインストール
  pip install Flask
  pip install boto3


# 実行
flask --app app run
　または  
python app.py