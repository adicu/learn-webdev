from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)
app.config["DEBUG"] = True  # Disable this for deployment

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/name")
def name():
    return "ADI"

@app.route("/website")
def website():
    return "http://adicu.com"

@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        url = "https://api.github.com/search/repositories?q=" + request.form["user_search"]
        response_dict = requests.get(url).json()
        return jsonify(response_dict)
    else: # request.method == "GET"
        return render_template("search.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
