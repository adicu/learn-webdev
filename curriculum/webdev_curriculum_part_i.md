<a id="top"></a>
# WebDev Curriculum Part 1

*Building a Server with Python and Flask*

Much of this tutorial is adapted from the [Flask website](http://flask.pocoo.org/).

-------------------

<a id="what-is-flask"></a>
## 1.0 What is Flask

[Flask](http://flask.pocoo.org/) is a microframework for Python.  It lets you build web apps using Python.  It is very easy to setup and has excellent documentation on it's [website](http://flask.pocoo.org/).  

<a id="how-a-flask-app-works"></a>
### 1.0.1 How a Flask App Works

Flask works with a [client-server model](http://en.wikipedia.org/wiki/Client%E2%80%93server_model).  The client, written in Python, has functions that take requests from clients and return web content to be displayed by the client.  Flask servers have the ability of serving [dynamic web pages](http://en.wikipedia.org/wiki/Dynamic_content), or pages that are generated every time you load the page.  For example, dynamic content could be of such pages include information stored in a database or a user account.

-------------------

<a id="the-autonomy-of-a-flask-app"></a>
## 1.1 The Anatomy of a Flask App

This is a very basic directory structure for a Flask webapp.

	ProjectDirectory/
	├── app.py
	├── requirements.txt
	├── static/
	│   ├── css/
	│   ├── img/
	│   └── js/
	└── templates/

-	`ProjectDirectory/` - Everything for your app goes in this folder.  Rename this to the name of your app.
-	`app.py` - All of the Python/Flask code and server logic gets written in this file.
-	`requirements.txt` - A list of all of the dependancies for your project.  See more about dependancies and installing them in [Section 0.1]().
-	`static/` - This folder holds all your static files.  Static files include:
	-	`js/` - Javascript files.
	-	`css/` - CSS files.
	-	`img/` - Image files.
-	`templates/` - This folder holds all your Flask templates.  Our HTML files will go here.  There are special features offered by Flask that make templates different than basic HTML files, explored in [Section 0.2]().

-------------------

<a id="hello-world"></a>
## 1.2 Hello World

In order to write the Hello World app, we only need to edit one file: `app.py`.  It's that easy!

<a id="editing-app-py"></a>
### 1.2.1 Editing app.py

First, import the `Flask` library from the `flask` package.

	from flask import Flask

Then, construct the Flask `app` variable.  We'll pass around this variable whenever we want to access information about the server

	app = Flask(__name__)
	
Next, apply the `@app.route("/")` decorator to a function called `hello()`.  It returns just the string `"Hello World!"`.  By doing this, we are making a [route](http://flask.pocoo.org/docs/quickstart/#routing).  The `route()` decorator binds the URL `http://yourapp.com/` to this function, effectively adding a new page to your app.  Functions with the `route()` decorator can return text strings or HTML, and whatever is returned will be displayed by the client.
	
	@app.route("/")
	def hello():
	    return "Hello World!"
	    
Finally, call `app.run()` when the file is executed.  Once `app.run()` is called, the server will start accepting requests from the client.
	
	if __name__ == "__main__":
	    app.run()

This leaves us with a completed Hello World program in Flask:

	from flask import Flask
	
	app = Flask(__name__)
	
	@app.route("/")
	def hello():
	    return "Hello World!"
	
	if __name__ == "__main__":
	    app.run()

<a id="running-a-flask-app"></a>
### 1.2.2 Running a Flask App

To run our Hello World app, just type the following command in the Project Directory folder:

	$ python app.py
	
If it's working, it should print the lines:

	* Running on http://127.0.0.1:5000/

Point your browser to that URL and bask in the awesomeness!  

<a id="developing-with-flask"></a>
### 1.2.3 Developing with Flask

Flask is great for development.  It offers very helpful error messages and prints stack traces well in the browser, if instructed to.  To enable these debugging features and (more importantly) automatic reload, edit `app.py` and add a statement configuring the `app` object.
	
	from flask import Flask
	
	app = Flask(__name__)
	app.config["DEBUG"] = True  # Disable this for deployment
	
	@app.route("/")
	def hello():
	    return "Hello World!"
	
	if __name__ == "__main__":
	    app.run()

With this modification, edit the string returned by the `hello()` function and refresh your browser to watch it change!  When you run the server now, it should also print:
	
	* Restarting on reloader
