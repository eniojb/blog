from flask import Flask

app = Flask("Hello")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/contatos")
def contato():
        return """<html>
            <head>
                <Contatos>
            </head>
            <body>
                <h1>Enio J.Barboza</h1>
                <h2>enio.email@email.com</h2>
                <h3>Contato: 119999-9999</h3>
            </body>
        </html>"""
    
