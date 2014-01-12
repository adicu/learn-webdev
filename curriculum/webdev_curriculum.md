<a id="top"></a>
# An Accelerated Introduction to Web Development

*Building a webapp in Flask.*

Much of this tutorial is adapted from the [Flask website][flask].  Written and developed by [Dan Schlosser](mailto:dan@adicu.com) and [ADI](http://adicu.com).

<a id="about-this-document"></a>
## About This Document

<a id="methodology"></a>
### Methodology

For the purposes of learning to make a web application using [Flask](#flask), we will write an entire web application, taking time to dissect how each piece functions and fits.  Each section is intended to be modular, but working in order is recommended.

<a id="the-end-product"></a>
### The End Product

We will be building a web application throughout this series, called "Has it Been Made Yet?".  It should let users type in a few keywords for a hackathon idea, and then it will tell them whether or not someone has made that idea and hosted it on [GitHub][github].  GitHub is a social network for [open-source][open-source] code, and is the most popular place for programmers to host their projects (and therefore, a great place to check for our app).

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
		-	[2.2.1 Determining the Request URL](#determining-the-request-url)
		-	[2.2.2 Using cURL](#using-curl)
		-	[2.2.3 Using Python](#using-python)
		-	[2.2.4 Using Flask: Extending the Search Route](#using-flask-extending-the-search-route)
		-	[2.2.5 Extension: Parsing JSON](#parsing-json)
		-	[2.2.6 Extension: Using JavaScript](#using-javascript)
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

[Flask][flask] is a microframework for Python.  It lets you build web apps using Python.  It is very easy to setup and has excellent documentation on its [website][flask].

<a id="how-a-flask-app-works"></a>
### 1.1.1 How a Flask App Works

Flask works with a [client-server model][client-server].  The server, written in Python, has functions that take requests from clients (i.e. your web browser) and return web content to be displayed by the client.  Flask servers have the ability of serving [dynamic web pages][dynamic-content], or pages that are generated every time you load the page.  For example, dynamic content could be of such pages include information stored in a database or a user account.

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

Next, apply the `@app.route("/")` [decorator][decorators] to a function called `hello()`.  It returns just the string `"Hello World!"`.  By doing this, we are making a [route][route].  The `route()` decorator binds the URL `http://yourwebapp.com/` to this function, effectively adding a new page to your app.  Functions with the `route()` decorator can return text strings or HTML, and whatever is returned will be displayed by the client.

```python
@app.route("/")
def hello():
    return "Hello World!"
```

Finally, call `app.run()` when the file is executed.  Once `app.run()` is called, the server will start accepting requests from the client.

```python
if __name__ == "__main__":
    app.run()
```

This leaves us with a completed Hello World program in Flask:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

<a id="running-a-flask-app"></a>
### 1.2.2 Running a Flask App

To run our Hello World app, just type the following command in the Project Directory folder:

	$ python app.py

If it's working, it should print the lines:

	* Running on http://127.0.0.1:5000/

Point your browser to that URL and bask in the awesomeness!

> Wondering what that weird URL is?  `127.0.0.1` is the IP address for [localhost][localhost], or your local computer.  When we run a Flask server with `python app.py`, it is running only on your machine, not the internet.  The `:5000` bit is the [port][port], or specific place where your app is running.  Developing locally is much easier and safer than publishing your app to the internet every time you want to test something, and is considered good practice.  Also, instead of typing out `http://127.0.0.1:5000` every time you want to see your app, you can also point your browser to `http://localhost:5000`.  The two are equivalent.

<a id="developing-with-flask"></a>
### 1.2.3 Developing with Flask

Flask is great for development.  It offers very helpful error messages and prints stack traces well in the browser, if instructed to.  To enable these debugging features and (more importantly) automatic reload, edit `app.py` and add a statement configuring the `app` object.

```python
from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True  # Disable this for deployment

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

With this modification, edit the string returned by the `hello()` function and refresh your browser to watch it change!  When you run the server now, it should also print:

	* Restarting on reloader

<a id="working-with-routes"></a>
## 1.3 Working with Routes

Let's define a few more routes for our app. Again, [routes][route] are URLs that are supported by the server. We use the [decorator][decorators] `app.route()` to tie the decorated function to the URL given in the parenthesis.

<a id="static-routes"></a>
### 1.3.1 Static Routes

First, lets make a route that lets the client get the name of the creator of this app.  Start by defining a function called `name()`, and have it return your name as a string.


```python
def name():
  return "Your Name"
```

Now we'll apply the decorator `route()`.  inside the parenthesis for the decorator, include the path `"/name"`.  Paths in Flask always start with a `/`.

```python
@app.route("/name")
def name():
  return "Your Name"
```

Save.  With your server [running](#running-a-flask-app) or [reloaded](#developing-with-flask),  point your browser to `"http://localhost:5000/name"` and your name will appear!  Our `/name` route is static, because it returns the same string every time.

Now, make another static route accessible at `http://localhost:5000/website` that returns the URL of your Github, Twitter, or personal website (don't forget the `http://`!). We'll use this route later.

> We won't show the code for the website route here, but it's implementation is in the sample code for your reference.

<a id="dynamic-routes"></a>
### 1.3.2 Dynamic Routes

Dynamic routes are what make using Flask so valuable.  Start off by making a static route called `search`.  It can return any string you want.  We'll edit it to return the results of our web search.

```python
@app.route("/search")
def search():
  return "Search"
```

To make our route dynamic, first we will modify the url to take a variable parameter named `search_query`.

```python
@app.route("/search/<search_query>")
```

Then, modify the `search` function to take a string parameter `search_query`, and return that.

```python
@app.route("/search/<search_query>")
def search(search_query):
  return search_query
```

Save and reload your server as needed, and navigate to `http://localhost:5000/search/test` and see `test` appear as the returned page.  If you change what comes after the `/search/` in the URL, it will be displayed in the browser.  We will soon modify this route to return actual search results.

------------------------

<a id="apis"></a>
# 2.0 APIs

<a id="api-basics"></a>
## 2.1 API Basics

At this point, our server can handle searches to our system, but it doesn't do anything with them (it just spits them back out).  What we need next is to search Github for projects with the same keywords and return them to the client.  To do this, we will use Github's [API][api], or Application Programmer Interface.

This section will take a step aside from our Flask project to build a foundation of knowledge around APIs and how they are used.  We will return to our app in [section 2.2](#the-github-search-api).

<a id="rest-apis"></a>
### 2.1.1 REST APIs

API's let us access external data in an easy, standardized way.  In the webapp world, when we say API we usually mean [REST (or RESTful) API][rest-api], which can be effectively thought of as an API that is accessible at a series of URL addresses. An extremely simple example of a REST API is [placekitten.com](http://placekitten.com), an API that serves images of kitten.  Here's how it works.  If you point your browser to `http://placekitten.com/<width>/<height>`, it returns an picture of kittens with that width and height. If you go to `/g/<width>/<height>` the image will be grayscale.  Go to these urls to see a very basic REST API in action.

URL | Image
------|-----
[`http://placekitten.com/200/100`](http://placekitten.com/200/100) | ![http://placekitten.com/200/100](http://placekitten.com/200/100)
[`http://placekitten.com/300/250`](http://placekitten.com/300/250) | ![http://placekitten.com/200/300](http://placekitten.com/300/250)
[`http://placekitten.com/g/300/250`](http://placekitten.com/g/300/250) | ![http://placekitten.com/g/200/300](http://placekitten.com/g/300/250)

The advantage in using a REST API here is that we don't need to remember the URL of the image we want, just the qualities (grayscale, 500x500).  Then, using the *documentation* provided at [placekitten.com](http://placekitten.com), we can derive the URL necessary to find the image we want.

> Many web designers use placeholder image APIs like [placekitten.com](http://placekitten.com) or [placehold.it](http://placehold.it) in their designs, as they speed up prototyping.

<a id="the-anatomy-of-a-url"></a>
### 2.1.2 The Anatomy of a URL

From here out we will be using some increasingly complex [URLs][urls], and it is important to develop a vocabulary for the parts of the url and their purpose.  To do this, we will dissect this url (which we will use in [section 2.2](#the-github-search-api) when we work with Github's API):

	https://api.github.com/search/repositories?q=tetris+language:assembly&sort=stars&order=desc

This URL breaks up into five parts:

1.	The protocol (`https`): We are using the [HTTPS][https] protocol, which is a secure version of HTTP, detailed in [section 2.1.5](#http).
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

> This URL schema is by no means complete; it encompasses the parts of a URL that are most relevant to API programming.  For a more complete view, check out [this blog post][url-google] by Google's Matt Cutts, or this exhaustive [Wikipedia entry][url-wikipedia].

<a id="data-in-json"></a>
### 2.1.3 Data in JSON

The data that we usually want to get from a RESTful API is text, not images, and to organize this text we use the [JSON][json], or JavaScript Object Notation text format.  JSON is a text format that makes data easy to read and simple to manipulate.  Here's a quick rundown:

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

To view JSON in the browser, use a browser extension like JSONView ([Chrome][json-chrome], [Firefox][json-firefox]) or JSON Formatter ([Safari][json-safari]).  Install the appropriate extension and reload [that url](http://www.colr.org/json/color/e0d1dd).  You should now see the JSON with the proper indentation that we like.  If that didn't work for you or you're using another browser, copy the mess into [jsonprettyprint.com](http://jsonprettyprint.com/) to see it nicely formatted.

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

<a id="http"></a>
### 2.1.5 Extension: HTTP

*If you don't remember the [client-server model][client-server], you should review it before reading this section.*

By now, you've seen "HTTP" in every URL in this document. Let's look a little at what "HTTP" actually means.

"HyperText Transfer Protocol" is the protocol by which your browser asks for and receives web sites (and lots of other
data). A web server sits around and listens for an *HTTP request*, which is when a web browser or other client asks for
a particular item (ex. web page or image) that the server has. An HTTP request looks something like this:

    GET /index.html HTTP/1.1
    Host: www.google.com
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0

There's a lot going on here, but you only need to pay attention to a few parts:

* `GET`: this is what we call an *HTTP verb*. This tells the web server what the client wants it to do. `GET` means
  "give me a resource"; `POST` means "here is some data"; `DELETE` means "get rid of this resource".

* `/index.html`: this indicates the resource that should be acted upon (using the given verb).

* `HTTP/1.1`: this is the HTTP version; it's almost always 1.1 (which has been
  around since 1999).

* The lines that begin with a word or phrase followed by a colon are called *headers*. They convey additional
  information. `Host` is the header that indicates what site the client wanted to access. `User-Agent` is the program
  that you're using as a client; here, it's Firefox.

Then, the server processes the request and sends back an *HTTP response*:

    HTTP/1.1 200 OK
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    ETag: "3f80f-1b6-3e1cb03b"
    Content-Type: text/html; charset=UTF-8
    Content-Length: 131
    Connection: close

    <html>
    <head>
      <title>An Example Page</title>
    </head>
    <body>
      Hello World, this is a very simple HTML document.
    </body>
    </html>

The first line includes the HTTP version that the server is using, followed by an *HTTP status code* and reason. Here,
the status is `200` and the reason is `OK`. This means that all went well.

* Status codes in the 100s are informational messages; you don't need to worry about them most of the time.
* Status codes in the 200s mean that the request was processed successfully.
* Status codes in the 300s mean that the client must do something else in order to complete the request successfully; an
  example is a redirect message (301).
* Status codes in the 400s mean that the client did something wrong; for example, code 404 means that the resource the
  client asked for could not be found by the server.
* Status codes in the 500s mean that something is wrong with the server; code 500 is a generic error message.

Then, there are a bunch of headers. After that is a blank line, then the *body* of the response (that is, the actual
data requested).

After the body of the response, the server closes the connection. To request another resource, the client must begin the
whole process again.

Check out the HTTP requests your browser makes! In Firefox, hit `Ctrl-Shift-Q` to open the network tool, or in Chrome,
hit `Ctrl-Shift-I` to open Developer tools and navigate to the "Network" tab (Mac users should use `Cmd` instead). Then,
browse the internet a little. Check out [here](http://www.example.com) for an example of a successful request, and
[here](http://www.adicu.com/notfound) for an example of an unsuccessful request.

<a id="the-github-search-api"></a>
## 2.2 The GitHub Search API

In order to figure out whether or not someone has made the app that was searched for using the our search route (started in [1.3.2](#dynamic-routes)), we'll use the Github Search API.  The first step for using any API is to familiarize yourself with its documentation, and so our first stop is [developer.github.com/v3/search][github-search-docs].  We know that we want to search for repositories, so we'll focus on the ["Search repositories" section][github-search-docs-repos].

<a id="determining-the-request-url"></a>
### 2.2.1 Determining the Request URL

Before we can try to parse Github search data, we need to determine the correct request URL, including the correct query string.  We know the protocol, domain, and path.  Don't forget the `https`!

	https://api.github.com/search/repositories

Now let's examine the query string piece by piece.

For the `q` key, we want the search query.   For our testing we'll use `Space Invaders HTML5`.  We have to encode that string to be URL safe, so we'll use `Space%20Invaders%20HTML5` (The space character needs to be encoded to `%20`).

	https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5

Sorting by best match makes sense, so we'll leave the `sort` key alone.  Descending order also seems fine, so we can leave the `order` key alone as well.

Github also provides search qualifiers, which can be added on to the `q` value.  It makes sense to limit our results to JavaScript projects, given that we're searching for HTML5 projects:

	https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5+language:JavaScript

If you put that URL into your browser, you should see the JSON response!


<a id="using-curl"></a>
### 2.2.2 Using cURL

*If you are using Windows, you may have to skip this section.  We will be using the cURL program, which is pre-installed on Mac and Linux machines.  It is possible to [install it on Windows][curl-win], but we won't walk through that process here.*

The most basic way of interaction with an API call programmatically is through the command line.  The [cURL](curl) program runs in Terminal, and is used (most simply) to copy the content at a URL and print it to the screen.  First, open Terminal.  If you are on a Mac, open Finder, click `Applications` on the sidebar, open the `Utilities` folder, and then double click `Terminal`.

Change directory into your *working directory*, or the directory where `app.py` is.

Type the following command:

	$ curl https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5+language:JavaScript

You should see the entire JSON response (probably pretty long!) print to the console.  Now lets write that response to a file:

	$ curl https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5+language:JavaScript > response.json

> The `> response.json` section redirects all the output that would normally be sent to the console into the `response.json` file.

You should now have a new file in your current directory named `response.json`.  If you open that file in your text editor, you'll see the response!

<a id="using-python"></a>
### 2.2.3 Using Python

Python has several built in libraries for handling REST APIs, but the external library [Requests][py-requests].  To install it, use [Pip][pip]:

	$ pip install requests

Don't forget to update your `requirements.txt` file to reflect this change!

Create a new python file:

	$ touch github.py

Editing `github.py`, start by importing requests.

```python
import requests
```

Now all we need to to is call `requests.get()` on the API url we developed in [section 2.2.1](#determining-the-request-url).  This method returns a [Response object][py-response-obj]. Add a print statement to see what the object is.

```python
import requests

url = "https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5+language:JavaScript"
response = requests.get(url)

print response
```

If you run this script, you should just see the Response object, represented by it's status code (hopefully `200`, or "OK").

	`$ python github.py`
	<Response [200]>

The only other thing we need is to get usable data is to convert the response object into a Python dictionary, using the Response object's `.json()` method.  To show that it worked, print it to stdout.

```python
import requests

url = "https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5+language:JavaScript"
response = requests.get(url)
response_dict = response.json()

print response_dict
```

This gives us, again a very large dictionary, printed to the screen.

> Try exploring the dictionary!  JSON has analogous structures in Python: objects become dictionaries, arrays become lists, and everything else converts as you expected.  For example, if you modify the print statement like so:
>
>	   print response_dict["items"][0]["language"]
>
> You should see it print "JavaScript", the language of the first repository returned from the API call.

<a id="using-flask-extending-the-search-route"></a>
### 2.2.4 Using Flask: Extending the Search Route

Adapting our Python code to work in our search route will be pretty simple, but there are a few constraints:

-	We want to search Github for the search query that the client sends, not our test string "Space Invaders HTML5"
-	We need to return valid HTML in our route, not a Python dictionary or a Response object.

Addressing the first issue is simple.  We'll let the `url` string be the base search URL concatenated with the `search_query` variable.

```python
from flask import Flask
import requests
...
@app.route("/search/<search_query>")
def search(search_query):
  url = "https://api.github.com/search/repositories?q=" + search_query
...
```

Then we know how to make a Response object from that url, but how do we make valid HTML?  Enter Flask's [`jsonify()`][flask-jsonify] method.  First, import it.

```python
from flask import Flask, jsonify
import requests
...
```

`jsonify` takes in a tree of dictionaries and arrays and converts it into JSON text (which is valid HTML).  Make `response_dict`, and return it jsonified.

```python
...
@app.route("/search/<search_query>")
def search(search_query):
  url = "https://api.github.com/search/repositories?q=" + search_query
  response_dict = requests.get(url).json()
  return jsonify(response_dict)
...
```

With your Flask server running, navigate to `localhost:5000/search/Space%20Invaders%20HTML5` and see all the results right in your browser (full circle!).

Try changing what comes after the `/search/` and see the results change.  Note that Github limits us to five requests per minute because of their [rate limiting][github-rate-limiting], but we will increase that number when we implement Authentication in [section 2.3](#authentication).

<a id="parsing-json"></a>
### 2.2.5 Extension: Parsing JSON

The JSON response that Github sends us is extremely long, and full of URLs that we don't need for our app.  We can't do anything about what they send us, but we it would be good practice to minimize the amount of data being sent to the client.

All we real need from each repo item in the `items` array is:

-	`name`,
-	`owner` (with `login`, `avatar_url`, and `html_url`),
-	`html_url`, and
-	`description`

We should also keep the `total_count` key-value pair.

> Have you noticed that the `total_count` is higher than the size of the `items` array?  That's because there are actually more results that are returned, but Github *paginates* their results, offering 30 results at a time by default to reduce the amount of data being sent per-request.  You can access all the results by passing in some extra information in the query string of the request, a process which is detailed in the ["pagination" section][github-api-docs-pagination] of the Github API documentation.

With just this data we can display an attractive list of the Github repos for the user's search query in [section 3.2](#templating-in-flask).

Write a function that takes in `response_dict` and returns a cleaned up dictionary that maintains the structure of `response_dict` but only has the keys enumerated above.  Pass this `response_dict` through this function before calling `jsonify()` on it.

<a id="using-javascript"></a>
### 2.2.6 Extension: Using JavaScript

*If you're familiar with JavaScript and would prefer to interact with the GitHub API using JavaScript, we'll go over how
to do that in this section. If you don't know JavaScript, feel free to skip it.*

Vanilla JavaScript has a way to interact with external APIs, but [jQuery](http://jquery.com/), a library of common
functions that simplifies your JavaScript, makes everything much easier. To include it, put the following line on your
HTML page:

    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>

After this is run, jQuery will be bound to the `$` object. All calls beginning with `$` are jQuery-related.

jQuery makes selecting DOM elements (that is, the HTML elements on your web page) incredibly simple using
[selectors](http://api.jquery.com/category/selectors/): to "select" all of the `img` elements on your page, do
`$("img")`; to select an element with id `example-id`, do `$("#example-id")`. Once an element is selected, you can
perform a number of actions with it; a fun one is `.fadeOut()`. See more at the
[jQuery API Documentation](http://api.jquery.com/).

jQuery also lets you perform *AJAX* (Asynchronous JavaScript and XML) requests easily. This is a mechanism that your
JavaScript can use to fetch new data without loading a new page (it's how your GMail inbox knows you have a new message
without you refreshing the page). That looks like this:

    $.getJSON("https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5+language:JavaScript&callback=?", function(data) {
        console.log(data);
    });

Here (as before), we fetch all repositories that match the string "Space Invaders" and are written in JavaScript; we
then print it out to the JavaScript console (which can be accessed in the "Developer Tools" for Firefox (`Ctrl-Shift-K`)
or Chrome (`Ctrl-Shift-J`) (or `Cmd` for OS X).

A couple of gotchas here:

* We add the parameter `callback=?`; this is a [JSONP](https://en.wikipedia.org/wiki/JSONP) callback to get around the
  [same-origin policy](https://en.wikipedia.org/wiki/Same-origin_policy). It's necessary for security reasons; for more
  information, see those links.

* We process the data in a *callback* (that's the `function(data) { ... }` bit). This is because loading data over the
  internet takes time; rather than stop everything up while we're waiting for that to finish, JavaScript moves on and
  executes the next statement. We tell JavaScript what we want it to do once it's finished loading the data; that's the
  body of the function we pass to `getJSON`.

That's it! You've successfully queried GitHub's API using JavaScript and jQuery.

<a id="authentication"></a>
## 2.3 Authentication

If you refresh your web browser enough times, you might see an error message instead of the expected JSON data.  This is because we are sending unauthorized requests to Github's API, meaning that we are using their API without logging in first.



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
[github]: http://github.com
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
[curl-win]: http://curl.haxx.se/download.html
[curl]: http://curl.haxx.se/docs/manpage.html
[py-requests]: http://docs.python-requests.org/en/latest/
[pip]: http://www.pip-installer.org/en/latest/
[py-response-obj]: http://docs.python-requests.org/en/latest/api/#requests.Response
[flask-jsonify]: http://flask.pocoo.org/docs/api/#flask.json.jsonify
[github-rate-limiting]: http://developer.github.com/v3/#rate-limiting
[github-api-docs-pagination]: http://developer.github.com/v3/#pagination
