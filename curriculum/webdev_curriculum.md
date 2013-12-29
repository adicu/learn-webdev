<a id="top"></a>
# An Accelerated Introduction to Web Development

*Building a webapp in Flask.*

Much of this tutorial is adapted from the [Flask website](flask).  Written by [Dan Schlosser](mailto:dan@adicu.com).

<a id="table-of-contents"></a>
## Table of Contents

-	[1.0 Flask](#flask)
	-	[1.1 What is Flask](#what-is-flask)
		-	[1.1.1 How a Flask App Works](#how-a-flask-app-works)
		-	[1.1.2 The Anatomy of a Flask App](#the-anatomy-of-a-flask-app)
		-	[1.1.3 Dependancies in Python](#dependancies-in-python)
	-	[1.2 Hello World](#hello-world-in-flask)
		-	[1.2.1 Editing app.py](#editing-app-py)
		-	[1.2.2 Running a Flask App](#running-a-flask-app)
		-	[1.2.3 Developing with Flask](#developing-with-flask)
	-	[1.3 Working with Routes](#working-with-routes)
		-	[1.3.1 Static Routes](#static-routes)
		-	[1.3.2 Dynamic Routes](#dynamic-routes)
-	[2.0 APIs](#apis)
	-	[2.1 API Basics](#api-basics)
		-	[2.1.1 What is an API](#what-is-an-api)
		-	[2.1.2 Data in JSON](#data-in-json)
		-	[2.1.3 Extension: Types of Requests](#types-of-requests)
	-	[2.2 The GitHub Search API](#the-github-search-api)
		-	[2.2.1 Using cURL](#using-curl)
		-	[2.2.2 Using Python](#using-python)
		-	[2.2.3 Using Flask: Extending the Search Route](#using-flask-extending-the-search-route)
		-	[2.2.4 Extension: Parsing JSON in Flask](#parsing-json-in-flask)
		-	[2.2.5 Extension: Using JavaScript](#using-javascript)
	-	[2.3 Authentication](#authentication)
		-	[2.3.1 Basic Authentication](#basic-authentication)
		-	[2.3.2 Extension: OAuth](#oauth)
-	[3.0 HTML and Templating](#html-and-css)
	-	[3.1 HTML Basics](#html-basics)
		-	[3.1.1 What is HTML](#what-is-HTML)
		-	[3.1.2 Anatomy of an HTML Document](#anatomy-of-an-html-document)
		-	[3.1.3 An Overview of Common Tags](#an-overview-of-common-tags)
	-	[3.2 Templating in Flask](#templating-in-flask)
		-	[3.2.1 A Simple Example: index.html](#a-simple-example-index-html)
		-	[3.2.2 Extending Templates](#extending-templates)
		-	[3.2.2 Template Variables](#template-variables)
-	[4.0 CSS](#css)
	-	[4.1 CSS Basics](#css-basics)
		-	[4.1.1 Selectors](#selectors)
		-	[4.1.2 CSS Best Practices](#css-best-practices)
	-	[4.2 External Libraries](#external-libraries)
		-	[4.2.1 Installation and Template Setup](#installation-and-template-setup)
		-	[4.2.2 Using Foundation](#using-foundation)
		-	[4.2.3 Rewriting Templates](#rewriting-templates)
		-	[4.2.4 Extension: Using Icon Fonts](#using-icon-fonts)

------------------------

<a id="flask"></a>
# 1.0 Flask

<a id="what-is-flask"></a>
## 1.1 What is Flask

[Flask](flask) is a microframework for Python.  It lets you build web apps using Python.  It is very easy to setup and has excellent documentation on its [website](flask).

<a id="how-a-flask-app-works"></a>
### 1.1.1 How a Flask App Works

Flask works with a [client-server model](client-server).  The server, written in Python, has functions that take requests from clients (i.e. your web browser) and return web content to be displayed by the client.  Flask servers have the ability of serving [dynamic web pages](dynamic-content), or pages that are generated every time you load the page.  For example, dynamic content could be of such pages include information stored in a database or a user account.

<a id="the-anatomy-of-a-flask-app"></a>
### 1.1.2 The Anatomy of a Flask App

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
-	`requirements.txt` - A list of all of the dependancies for your project.  See more about dependancies and installing them in [the next section](#dependancies-in-python).
-	`static/` - This folder holds all your static files.  Static files include:
	-	`js/` - Javascript files.
	-	`css/` - CSS files.
	-	`img/` - Image fls.
-	`templates/` - This folder holds all your Flask templates.  Our HTML files will go here.  There are special features offered by Flask that make templates different than basic HTML files, explored in [Section 3.2](#templating-in-flask).

<a id="dependancies-in-python"></a>
### 1.1.3 Dependancies in Python

TODO: Question: will this section already be covered in the intro to Python workshop on Saturday?

<a id="hello-world-in-flask"></a>
## 1.2 Hello World in Flask

In order to write the Hello World app, we only need to edit one file: `app.py`.  It's that easy!

<a id="editing-app-py"></a>
### 1.2.1 Editing app.py

First, import the `Flask` class from the `flask` module.

	from flask import Flask

Then, construct the Flask `app` variable.  We'll pass around this variable whenever we want to access information about the server. We pass `__name__` into the `Flask()` function so that your flask app is associated with the directory structure we created in [Section 1.1](#the-anatomy-of-a-flask-app).

	app = Flask(__name__)

Next, apply the `@app.route("/")` [decorator](decorators) to a function called `hello()`.  It returns just the string `"Hello World!"`.  By doing this, we are making a [route](route).  The `route()` decorator binds the URL `http://yourwebapp.com/` to this function, effectively adding a new page to your app.  Functions with the `route()` decorator can return text strings or HTML, and whatever is returned will be displayed by the client.

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

> Wondering what that weird URL is?  `127.0.0.1` is the IP address for [localhost](localhost), or your local computer.  When we run a Flask server with `python app.py`, it is running only on your machine, not the internet.  The `:5000` bit is the [port](port), or specific place where your app is running.  Developing locally is much easier and safer than publishing your app to the internet every time you want to test something, and is considered good practice.  Also, instead of typing out `http://127.0.0.1:5000` every time you want to see your app, you can also point your browser to `http://localhost:5000`.  The two are equivalent.

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

<a id="working-with-routes"></a>
## 1.3 Working with Routes

Let's define a few more routes for our app. Again, [routes](route) are URLs that are supported by the server. We use the [decorator](decorators) `app.route()` to tie the decorated function to the URL given in the parenthesis.

<a id="static-routes"></a>
### 1.3.1 Static Routes

First, lets make a route that lets the client get the name of the creator of this app.  Start by defining a function called `name()`, and have it return your name as a string.

	def name():
		return "Your Name"

Now we'll apply the decorator `route()`.  inside the parenthesis for the decorator, include the path `"/name"`.  Paths in Flask always start with a `/`.

	@app.route("/name")
	def name():
		return "Your Name"

Save.  With your server [running](#running-a-flask-app) or [reloaded](#developing-with-flask),  point your browser to `"http://localhost:5000/name"` and your name will appear!  Our `/name` route is static, because it returns the same string every time.

Now, make another static route accessible at `http://localhost:5000/website` that returns the URL of your Github, Twitter, or personal website (don't forget the `http://`!). We'll use this route later.

> We won't show the code for the website route here, but it's implementation is in the sample code for your reference.

<a id="dynamic-routes"></a>
### 1.3.2 Dynamic Routes

Dynamic routes are what make using Flask so valuable.  Start off by making a static route called `search`.  It can return any string you want.  We'll edit it to return the results of our web search.

	@app.route("/search")
	def search():
		return "Search"

To make our route dynamic, first we will modify the url to take a variable parameter named `search_query`.

	@app.route("/search/<search_query>")

Then, modify the `search` function to take a string parameter `search_query`, and return that.

	@app.route("/search/<search_query>")
	def search(search_query):
		return search_query

Save and reload your server as needed, and navigate to `http://localhost:5000/search/test` and see `test` appear as the returned page.  If you change what comes after the `/search/` in the URL, it will be displayed in the browser.  We will soon modify this route to return actual search results.

------------------------

<a id="apis"></a>
# 2.0 APIs

<a id="api-basics"></a>
## 2.1 API Basics

<a id="what-is-an-api"></a>
### 2.1.1 What is an API

<a id="data-in-json"></a>
### 2.1.2 Data in JSON

<a id="types-of-requests"></a>
### 2.1.3 Extension: Types of Requests

<a id="the-github-search-api"></a>
## 2.2 The GitHub Search API

<a id="using-curl"></a>
### 2.2.1 Using cURL

<a id="using-python"></a>
### 2.2.2 Using Python

<a id="using-flask-extending-the-search-route"></a>
### 2.2.3 Using Flask: Extending the Search Route

<a id="parsing-json-in-flask"></a>
### 2.2.4 Extension: Parsing JSON in Flask

<a id="using-javascript"></a>
### 2.2.5 Extension: Using JavaScript

<a id="authentication"></a>
## 2.3 Authentication

<a id="basic-authentication"></a>
### 2.3.1 Basic Authentication

<a id="oauth"></a>
### 2.3.2 OAuth

------------------------

<a id="html-and-css"></a>
# 3.0 HTML and Templating

<a id="html-basics"></a>
## 3.1 HTML Basics

<a id="what-is-HTML"></a>
### 3.1.1 What is HTML

<a id="anatomy-of-an-html-document"></a>
### 3.1.2 Anatomy of an HTML Document

<a id="an-overview-of-common-tags"></a>
### 3.1.3 An Overview of Common Tags

<a id="templating-in-flask"></a>
## 3.2 Templating in Flask

<a id="a-simple-example-index-html"></a>
### 3.2.1 A Simple Example: index.html

<a id="extending-templates"></a>
### 3.2.2 Extending Templates

<a id="template-variables"></a>
### 3.2.2 Template Variables

------------------------

<a id="css"></a>
# 4.0 CSS

<a id="css-basics"></a>
## 4.1 CSS Basics

<a id="selectors"></a>
### 4.1.1 Selectors

<a id="css-best-practices"></a>
### 4.1.2 CSS Best Practices

<a id="external-libraries"></a>
## 4.2 External Libraries

<a id="installation-and-template-setup"></a>
### 4.2.1 Installation and Template Setup

<a id="using-foundation"></a>
### 4.2.2 Using Foundation

<a id="rewriting-templates"></a>
### 4.2.3 Rewriting Templates

<a id="using-icon-fonts"></a>
### 4.2.4 Extension: Using Icon Fonts


[route]: http://flask.pocoo.org/docs/quickstart/#routing
[port]: http://en.wikipedia.org/wiki/Port_(computer_networking)
[localhost]: http://en.wikipedia.org/wiki/Localhost
[client-server]: http://en.wikipedia.org/wiki/Client%E2%80%93server_model
[flask]: http://flask.pocoo.org/
[dynamic-content]: http://en.wikipedia.org/wiki/Dynamic_content
[decorators]: https://wiki.python.org/moin/PythonDecorators

