from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def say_hello():
    return jsonify({"message": "manas says hi to you all"})


if __name__ == "__main__":
    app.run(port=6969, debug=True)