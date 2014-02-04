from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True  # Disable this for deployment

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/name")
def name():
    return "ADI"

@app.route("/website")
def website():
    return "http://adicu.com"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
