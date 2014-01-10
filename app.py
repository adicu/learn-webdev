from flask import Flask, jsonify
from sys import exit
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

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
    url = "https://api.github.com/search/repositories?q=" + search_query
    response_dict = requests.get(url,
        auth=(app.config['gh_username'], app.config['gh_password'])).json()
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

def get_github_token():
    gh_username = raw_input('GitHub username: ')
    gh_password = raw_input('GitHub password: ')

    gh_response = requests.get('https://api.github.com/user',
        auth=(gh_username, gh_password))

    if gh_response.status_code == 401:  # fail to authenticate
        print 'Sorry, your login information was incorrect, please try again'
        exit(1)

    return gh_username, gh_password

if __name__ == "__main__":
    username, password = get_github_token()
    app.config['gh_username'] = username
    app.config['gh_password'] = password 

    app.run()

