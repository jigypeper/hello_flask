from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function


@app.route('/')
@make_bold
def hello_world():
    return 'Hello, World!'

@app.route('/<name>/<int:number>')
def hello_name(name, number):
    return f"Hello {name}, you have {number} pies"

if __name__ == "__main__":

    app.run(debug=True)
