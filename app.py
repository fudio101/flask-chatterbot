# pip install git+https://github.com/dsdanielpark/Bard-API.git
from flask import Flask, render_template, request
from bardapi import BardCookies

app = Flask(__name__)
cookie_dict = {
    "__Secure-1PSID": "xxxx",
    "__Secure-1PSIDTS": "xxxx",
    "__Secure-1PSIDCC": "xxxx"
}

bard = BardCookies(cookie_dict=cookie_dict)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    query = request.args.get('msg')
    response = bard.get_answer(query)['content']

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=54321)
