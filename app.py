from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>GitHub Deployment Experiment</h1>
    <p>Python application is running successfully.</p>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
