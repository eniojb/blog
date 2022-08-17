from flask import Flask, render_template

app = Flask("Hello")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/usuario")
def usuario():
    usuario = [1, "Danilo de Souza Miguel", "Professor"]
    alunos =["Andre Guedes","Lucas Santos","Alicia Duarte","Raiane Carpline"] 
    return render_template("index.html", usuario = usuario, alunos = alunos)

@app.route("/contatos")
def contato():
    nomeAula = "Aula python para Web"   
    return render_template("index.html", nome = nomeAula)


