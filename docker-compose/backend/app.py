import random
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/roll", methods=["GET"])
def roll_dice():
    num_dice = request.args.get("num", 1, type=int)
    sides = request.args.get("sides", 6, type=int)

    num_dice = max(1, min(num_dice, 100))
    sides = max(2, min(sides, 100))

    results = [random.randint(1, sides) for _ in range(num_dice)]

    return jsonify({
        "num_dice": num_dice,
        "sides": sides,
        "results": results,
        "total": sum(results),
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
