from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True  # Disable this for deployment

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()