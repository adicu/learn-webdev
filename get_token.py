
from sys import exit
import requests
import json

payload = json.dumps({'scopes': [], 'note': 'search app'})
gh_username = raw_input('GitHub username: ')
gh_password = raw_input('GitHub password: ')

token_url = 'https://api.github.com/authorizations'
gh_response = requests.post(token_url, auth=(gh_username, gh_password),
        data=payload)

if gh_response.status_code >= 400:  # fail to authenticate
    print 'Sorry, your login information was incorrect, please try again'
    exit(1)

print "Here is your auth token\n-->\t" + gh_response.json()['token']
print "Add it to your settings file"

