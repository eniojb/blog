from flask import Flask, render_template
from datetime import datetime

app = Flask("Hello")

posts = [
    {
        "title": "Meu primeiro posts",
        "body": "Esse post é o primeiro do blog",
        "autor": "Danilo Souza Miguel",
        "created": datetime(2022,8,17)

    },
    {
        "title": "Meu segundo posts",
        "body": "Esse post é o primeiro do blog",
        "autor": "Danilo Souza Miguel",
        "created": datetime(2022,8,17)

    },
    {
        "title": "Meu terceiro posts",
        "body": "Esse post é o primeiro do blog",
        "autor": "Danilo Souza Miguel",
        "created": datetime(2022,8,17)

    }        
]


@app.route("/")
def index():
    return render_template("index.html", posts=posts)
