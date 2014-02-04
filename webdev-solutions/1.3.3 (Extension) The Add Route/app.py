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

@app.route("/search/<search_query>")
def search(search_query):
	return search_query

@app.route("/add/<x>/<y>")
def add(x, y):
	return str(int(x) + int(y))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
