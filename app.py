from flask import Flask, jsonify
import requests

username = "danrschlosser"
password = ""

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/name")
def name():
	return "Dan"

@app.route("/website")
def website():
	return "http://danrs.ch"

@app.route("/search/<search_query>")
def search(search_query):
	url = "https://api.github.com/search/repositories?q=" + search_query
	r = requests.get(url)
	return jsonify(r.json())

if __name__ == "__main__":
	app.run()