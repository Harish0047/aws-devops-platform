from flask import Flask, Response, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUESTS = Counter("app_requests_total", "Total requests", ["endpoint"])


@app.route("/")
def home():
    REQUESTS.labels(endpoint="/").inc()
    return "Hello from aws-devops-platform"


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
