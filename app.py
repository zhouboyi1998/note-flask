from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/hello/<name>')
def hello_world(name):  # put application's code here
    return jsonify({"message": f"Hello, {name}", "code": 200})


if __name__ == '__main__':
    app.run(port=18073)
