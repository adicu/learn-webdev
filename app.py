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
    if "items" not in response_dict:
        return jsonify(response_dict)
    else:
        return jsonify(parse_response(response_dict))

def parse_response(response_dict):
    clean_dict = {
        "total_count": response_dict["total_count"],
        "items":[]
    }
    for repo in response_dict["items"]:
        clean_repo = {
            "name": repo["name"],
            "owner": {
                "login": repo["owner"]["login"],
                "avatar_url": repo["owner"]["avatar_url"],
                "html_url": repo["owner"]["html_url"]
            },
            "html_url": repo["html_url"],
            "description": repo["description"]
        }
        clean_dict["items"].append(clean_repo)
    return clean_dict

if __name__ == "__main__":

    app.run()

