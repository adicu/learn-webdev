from flask import Flask, jsonify
from os import environ
from sys import exit
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

try:
    app.config['gh_token'] = environ['gh_token']
except KeyError:
    print 'GitHub token missing from environment variables.'
    exit(1)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/name")
def name():
    return "ADI"

@app.route("/website")
def website():
    return "http://adicu.com"

@app.route("/search/<search_query>")
def search(search_query):
	url = "https://api.github.com/search/repositories"
	data = {
		'q': search_query,
		'access_token': app.config['gh_token']
	}
	response_dict = requests.get(url, params=data).json()
	return jsonify(response_dict)

if __name__ == "__main__":
    app.run()