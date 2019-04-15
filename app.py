from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, world!</h1>'


@app.route('/oi')
def fbh():
    return '<h1>Oi!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
