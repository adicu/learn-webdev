from flask import Flask, jsonify, render_template, request
from os import environ
from sys import exit
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

# try:
#     app.config['gh_token'] = environ['gh_token']
# except KeyError:
#     print 'GitHub token missing from environment variables.'
#     exit(1)

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
        print request.form
        url = "https://api.github.com/search/repositories"
        data = {
            'q': request.form["user_search"]#,
            # 'access_token': app.config['gh_token']
        }
        response_dict = requests.get(url, params=data).json()
        if "items" not in response_dict:
            return jsonify(response_dict)
        else:
            return render_template("results.html", api_data=response_dict)
    else: # request.method == "GET"
        return render_template("search.html")

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

