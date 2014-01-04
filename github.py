import requests

url = "https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5+language:JavaScript"
response = requests.get(url)
response_dict = response.json()

# The reponse object
# print response

print response_dict

# "JavaScript"
# print response_dict["items"][0]["language"]