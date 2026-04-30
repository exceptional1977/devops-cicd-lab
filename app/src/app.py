import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "service": "devops-cicd-lab",
        "version": os.environ.get("APP_VERSION", "1.0.0"),
        "hostname": os.environ.get("HOSTNAME", "unknown")
    })

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/greeting')
def greeting():
    flag = os.environ.get("FEATURE_NEW_GREETING", "false").lower() == "true"
    if flag:
        return jsonify({"greeting": "Hello from new feature!"})
    else:
        return jsonify({"greeting": "Hello, world!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
