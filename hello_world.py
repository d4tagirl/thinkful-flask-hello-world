from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/la/<name>/<surname>")
def hello_person(name, surname):
    html = """
        <h1>
            Hello {} {}!
        </h1>
        <p>
            Your Jedi name is {}{}!
        </p>
    """
    return html.format(name.title(), surname.title(), surname[:3], name[:2].lower())

# @app.route("/hello/la/<name>")
# def hello_person(name):
#     html = """
#         <h1>
#             Hello {}!
#         </h1>
#         <p>
#             Your Jedi name is {}.
#         </p>
#     """
#     return html.format(name.title())

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
