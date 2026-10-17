from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to CloudDeploy!"


@app.route("/health")
def health():
    return jsonify({
        "project": "CloudDeploy",
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)