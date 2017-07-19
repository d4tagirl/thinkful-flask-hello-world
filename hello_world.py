from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/la/<name>/<surname>")
def hello_person(name, surname):
  return render_template('template.html',
                         name = name.title(),
                         surname = surname.title(),
                         three_surname = surname[:3],
                         two_name = name[:2].lower())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
