<a id="top"></a>
# An Accelerated Introduction to Web Development

*Building a webapp in Flask.*

Much of this tutorial is adapted from the [Flask website](flask).  Written and developed by [Dan Schlosser](mailto:dan@adicu.com) and [ADI](http://adicu.com).

<a id="about-this-document"></a>
## About This Document

<a id="methodology"></a>
### Methodology

For the purposes of learning to make a web application using [Flask](#flask), we will write an entire web application, taking time to dissect how each piece functions and fits.  Each section is intended to be modular, but working in order is recommended.  

<a id="the-end-product"></a>
### The End Product

We will be building a web application throughout this series, called "Has it Been Made Yet?".  It should let users type in a few keywords for a hackathon idea, and then it will tell them whether or not someone has made that idea and hosted it on [GitHub](github).  GitHub is a social network for [open-source](open-source) code, and is the most popular place for programmers to host their projects (and therefore, a great place to check for our app).	

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
		-	[2.1.1 REST APIs](#rest-apis)
		-	[2.1.2 The Anatomy of a URL](#the-anatomy-of-a-url)
		-	[2.1.3 Data in JSON](#data-in-json)
		-	[2.1.4 Viewing JSON in the Browser](#viewing-json-in-the-browser)
		-	[2.1.5 Extension: HTTP](#http)
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
-	`requirements.txt` - A list of all of the dependancies for your project.  See more about dependancies and installing them in [SOME UNDETERMINED SECTION](#dependancies-in-python).
-	`static/` - This folder holds all your static files.  Static files include:
	-	`js/` - Javascript files.
	-	`css/` - CSS files.
	-	`img/` - Image fls.
-	`templates/` - This folder holds all your Flask templates.  Our HTML files will go here.  There are special features offered by Flask that make templates different than basic HTML files, explored in [Section 3.2](#templating-in-flask).

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

At this point, our server can handle searches to our system, but it doesn't do anything with them (it just spits them back out).  What we need next is to search Github for projects with the same keywords and return them to the client.  To do this, we will use Github's [API](api), or Application Programmer Interface.

This section will take a step aside from our Flask project to build a foundation of knowledge around APIs and how they are used.  We will return to our app in [section 2.2](#the-github-search-api).

<a id="rest-apis"></a>
### 2.1.1 REST APIs

API's let us access external data in an easy, standardized way.  In the webapp world, when we say API we usually mean [REST (or RESTful) API](rest-api), which can be effectively thought of as an API that is accessible at a series of URL addresses. An extremely simple example of a REST API is [placekitten.com](http://placekitten.com), an API that serves images of kitten.  Here's how it works.  If you point your browser to `http://placekitten.com/<width>/<height>`, it returns an picture of kittens with that width and height. If you go to `/g/<width>/<height>` the image will be grayscale.  Go to these urls to see a very basic REST API in action.

URL | Image
------|-----
[`http://placekitten.com/200/100`](http://placekitten.com/200/100) | ![http://placekitten.com/200/100](http://placekitten.com/200/100)
[`http://placekitten.com/300/250`](http://placekitten.com/300/250) | ![http://placekitten.com/200/300](http://placekitten.com/300/250)
[`http://placekitten.com/g/300/250`](http://placekitten.com/g/300/250) | ![http://placekitten.com/g/200/300](http://placekitten.com/g/300/250)

The advantage in using a REST API here is that we don't need to remember the URL of the image we want, just the qualities (grayscale, 500x500).  Then, using the *documentation* provided at [placekitten.com](http://placekitten.com), we can derive the URL necessary to find the image we want.

> Many web designers use placeholder image APIs like [placekitten.com](http://placekitten.com) or [placehold.it](http://placehold.it) in their designs, as they speed up prototyping.  

<a id="the-anatomy-of-a-url"></a>
### 2.1.2 The Anatomy of a URL

From here out we will be using some increasingly complex [URLs](urls), and it is important to develop a vocabulary for the parts of the url and their purpose.  To do this, we will dissect this url (which we will use in [section 2.2](#the-github-search-api) when we work with Github's API):

	https://api.github.com/search/repositories?q=tetris+language:assembly&sort=stars&order=desc
	
This URL breaks up into five parts:

1.	The protocol and separator (`https://`): We are using the [HTTPS](https) protocol, detailed in [section 2.1.5](#http).  
2.	The separator (`://`): A colon and two slashes always follow the protocol is used to separate the protocol and the host.
3.	The host (`api.github.com`): A host is usually a domain name (this is the case for our url), but it could also be an IP Address.
4.	The path (`/search/repositories`): Everything from the first `/` up to the `?` that starts the query string is the path. When accessing a web page, often these paths will be hierarchical and include a filename at the end, like `/blog/2014/02/post.html`.  When making API calls, these paths are the API method that is being called.  Here, we are searching repositories.
5.	The query string (`?q=tetris+language:assembly&sort=stars&order=desc`): is a series of key-value pairs of the form `<key>=<value>`. The query string starts with a `?` and each key-value pair is separated by `&`.  The key value pairs here are:
	
	Key | Value
	----|--------------------------
	`q` | `tetris+language:assembly`
	`sort` | `stars`
	`order` | `desc`
	
	>Note that the `+` and `:` do not denote keys or values, and are all part of the `q` value.  The inclusion of these characters is specific to Github's API, and we will learn more about why they are there in [section 2.2](#the-github-search-api).  From a URL standard perspective, `tetris+language:assembly` is one big value for the `q` key.  
	
	For the most part, the job of the query string is to specify the details of the data being returned.  While the `q` key is somewhat complicated, we can see clearly that the results of this search are being sorted by stars in descending order.
	
> This URL schema is by no means complete; it encompasses the parts of a URL that are most relevant to API programming.  For a more complete view, check out [this blog post](url-google) by Google's Matt Cutts, or this exhaustive [Wikipedia entry](url-wikipedia).

<a id="data-in-json"></a>
### 2.1.3 Data in JSON

The data that we usually want to get from a RESTful API is text, not images, and to organize this text we use the [JSON](json), or JavaScript Object Notation text format.  JSON is a text format that makes data easy to read and simple to manipulate.  Here's a quick rundown:

Most JSON documents start and end with braces (`{ }`).  We'll learn what these are later.

	{ }
	
The core element of JSON documents are key-value pairs.  A key is a string, and a value can be (amongst other things) a string. Keys and values are separated by a colon (`:`).

	{ "name": "Jane Doe" }
	
Whitespace non-significant, and should be added for readability.

	{
		"name": "Jane Doe"
	}

Multiple key-value pairs can be separated by commas (`,`).

	{
		"name": "Jane Doe",
		"occupation": "student",
		"school": "Columbia University"
	}

Values can also be decimal numbers, boolean values (`true` or `false`), or `null`.

	{
		"name": "Jane Doe",
		"age": 20,
		"female": true,
		"male": false,
		"occupation": "student",
		"school": "Columbia SEAS",
		"children": null
	}
	
Values can also be arrays.  Arrays are comma-separated values surrounded by brackets (`[ ]`).  Values in arrays should be all of the same type, but don't have to be.

	{
		"name": "Jane Doe",
		"age": 20,
		"female": true,
		"male": false,
		"occupation": "student",
		"school": "Columbia SEAS",
		"children": null,
		"hobbies": [
			"programming",
			"cello",
			"painting",
			"basketball",
			"REST APIs"
		],
		"luckynumbers" : [
			10, 25.3, 404
		]
	}

The final value type is objects.  Objects are a comma-separated key-value pairs surrounded by braces (`{ }`).  In fact, our entire JSON document is one big object.

	{
		"name": "Jane Doe",
		"age": 20,
		"female": true,
		"male": false,
		"occupation": "student",
		"school": {
			"fullname": "The Fu Foundation School of Engineering & Applied Science",
			"university": "Columbia University",
			"undergrad": true
		},
		"children": null,
		"hobbies": [
			"programming",
			"cello",
			"painting",
			"basketball",
			"REST APIs"
		],
		"luckynumbers" : [
			10, 25.3, 404
		]
	}

> Most JSON documents are one big object, but they can also be one big array:
>
>     [
>         "This",
>		  "Is",
>		  {
>		      "valid": JSON
>		  }
>	  ]

JSON can represent a wide variety of data, just using the simple types:

- Objects
- Arrays
- Strings
- Numbers
- Booleans
- `null`

<a id="viewing-json-in-the-browser"></a>
### 2.1.4 Viewing JSON in the Browser

JSON is the most common data format returned by RESTful APIs.  For example, [colr.org](http://colr.org)'s [API](http://colr.org/api.html) returns it's responses in JSON format.  Try it: point your browser to [http://www.colr.org/json/color/e0d1dd](http://www.colr.org/json/color/e0d1dd).  You'll probably see some unreadable mess like this:

	{"colors": [{"timestamp": 1187574833, "hex": "e0d1dd", 
	"id": 19425, "tags": 	[{"timestamp": 1111913422, "id": 
	11257, "name": "joyful"}, {"timestamp": 1108110854, 
	"id": 2798, "name": "lilac"}]}], "schemes": [], 
	"schemes_history": {}, "success": true, "colors_history": 
	{"e0d1dd": [{"d_count": 0, "id": "11257", "a_count": 1,
	 "name": "joyful"}, {"d_count": 0, "id": "2798", 
	 "a_count": 1, "name": "lilac"}]}, "messages": [], 
	 "new_color": "e0d1dd"}
	 
To view JSON in the browser, use a browser extension like JSONView ([Chrome](json-chrome), [Firefox](json-firefox)) or JSON Formatter ([Safari](json-safari)).  Install the appropriate extension and reload [that url](http://www.colr.org/json/color/e0d1dd).  You should now see the JSON with the proper indentation that we like.  If that didn't work for you or you're using another browser, copy the mess into [jsonprettyprint.com](http://jsonprettyprint.com/) to see it nicely formatted.

It should look like this:

	{
	  "colors": [
	    {
	      "timestamp": 1187574833,
	      "hex": "e0d1dd",
	      "id": 19425,
	      "tags": [
	        {
	          "timestamp": 1111913422,
	          "id": 11257,
	          "name": "joyful"
	        },
	        {
	          "timestamp": 1108110854,
	          "id": 2798,
	          "name": "lilac"
	        }
	      ]
	    }
	  ],
	  "schemes": [],
	  "schemes_history": {},
	  "success": true,
	  "colors_history": {
	    "e0d1dd": [
	      {
	        "d_count": 0,
	        "id": "11257",
	        "a_count": 1,
	        "name": "joyful"
	      },
	      {
	        "d_count": 0,
	        "id": "2798",
	        "a_count": 1,
	        "name": "lilac"
	      }
	    ]
	  },
	  "messages": [],
	  "new_color": "e0d1dd"
	}
	
So now that we see it nicely formatted, what are we seeing here?  

The document is one big object, with keys 	`colors`, `schemes`, `schemes_history`, `success`, `colors_history`, `messages`, and `new_color`.  The value associated with the key `colors` is an array containing one color object, which has the keys `timestamp`, `hex`, `id`, and `tags`.  The value associated with the key `tags` is also an array of objects, where each of these objects is a tag.

So how did we know that the array for `colors` held color objects and the array for `tags` holds tag objects?  We don't.  With JSON, we don't have strictly defined object types like many programming languages do.  We have to trust the creator of the JSON document to store their data in a consistent way.  Because the JSON we are reading is written well, the `tags` key has an array value that holds objects that look very similar and have the attributes of a tag.  The API call we are making is for one specific color, so it makes sense that array associated with the `colors` key has only color object in it.  

Try out these other API calls (`http://colr.org<path>`) to see how colr.org used this JSON structure to return different types of results:

Path | Description
----|------------
[`/json/color/e0d1dd`](http://www.colr.org/json/color/e0d1dd) | data for the color with hex value `e0d1dd`
[`/json/colors/e0d1dd,95604a`](http://www.colr.org/json/colors/e0d1dd,95604a) | data for the colors `e0d1dd` and `95604a`
[`/json/color/random`](http://www.colr.org/json/color/random) | data for random color
[`/json/colors/random/3`](http://www.colr.org/json/color/random/3) | data for three random colors 

<a id="types-of-requests"></a>
### 2.1.5 Extension: HTTP

<a id="the-github-search-api"></a>
## 2.2 The GitHub Search API

In order to figure out whether or not someone has made the app that was searched for using the our search route (started in [1.3.2](#dynamic-routes)), we'll use the Github Search API.  The first step for using any API is to familiarize yourself with its documentation, and so our first stop is to [developer.github.com/v3/search](github-search-docs).  We know that we want to search for repositories, so we'll focus on the ["Search repositories" section](github-search-docs-repos).

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
[api]: http://en.wikipedia.org/wiki/Api
[rest-api]: http://en.wikipedia.org/wiki/REST_API
[open-source]: http://en.wikipedia.org/wiki/Open_source
[json]: http://en.wikipedia.org/wiki/Json
[json-chrome]: https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc?hl=en
[json-firefox]: https://addons.mozilla.org/en-us/firefox/addon/jsonview/
[json-safari]: https://github.com/rfletcher/safari-json-formatter
[github-search-docs]: http://developer.github.com/v3/search/
[github-search-docs-repos]: http://developer.github.com/v3/search/#search-repositories
[https]: http://en.wikipedia.org/wiki/Https
[urls]: http://en.wikipedia.org/wiki/Uniform_resource_locator
[url-google]: http://www.mattcutts.com/blog/seo-glossary-url-definitions/
[url-wikipedia]: http://en.wikipedia.org/wiki/URI_scheme#Generic_syntax