# coding: utf-8

from flask import Flask, render_template

# Flaskをインスタンス化
app = Flask(__name__)

# --- Viewの設定 ---
# ルートディレクトリにアクセスした場合の挙動
@app.route('/')

# def以下がアクセス後の操作
def index():
    # DBから以下の変数を読み込んできたと仮定
    title_ = 'ようこそ'
    message_ = 'MTVデザインパターンでWebアプリ作成'

    # return 'Hello World!'
    return render_template('index.html', title=title_, message=message_)

if __name__ == '__main__':
    app.run()