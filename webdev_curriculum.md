<a id="top"></a>
# An Accelerated Introduction to Web Development
 
*Building a webapp in Flask.*

Written and developed by [Dan Schlosser](http://danrs.ch) and [ADI](http://adicu.com).

<a href="#top" class="top" id="about-this-document">Top</a>
## About This Document

<a id="methodology"></a>
### Methodology

For the purposes of learning to make a web application using [Flask](#flask), we will write an entire web application, taking time to dissect how each piece functions and fits.  Each section is intended to be modular, but working in order is recommended.

This document teaches the CSS and HTML programming languages, as well as the Flask Python library.

<a id="prerequisites"></a>
### Prerequisites

Basic knowledge of the Python programming language is suggested.  If you don't already know Python, checkout [this ADI-developed tutorial](http://adicu.com/intro-webdev/python).  No knowledge of HTML, CSS or Flask is expected or required.

<a id="the-end-product"></a>
### The End Product

We will be building a web application throughout this series, called "Has it Been Made Yet?".  It should let users type in a few keywords for a hackathon idea, and then it will tell them whether or not someone has made that idea and hosted it on [GitHub][github].  GitHub is a social network for [open-source][open-source] code, and is the most popular place for programmers to host their projects (and therefore, a great place to check for our app).

<a href="#top" class="top" id="table-of-contents">Top</a>
## Table of Contents

-	[1.0 Flask](#flask)
	-	[1.1 What is Flask](#what-is-flask)
		-	[1.1.1 How a Flask App Works](#how-a-flask-app-works)
		-	[1.1.2 The Anatomy of a Flask App](#the-anatomy-of-a-flask-app)
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
	-	[2.3 Extension: Authentication](#authentication)
		-	[2.3.1 Extension: Basic Authentication](#basic-authentication)
-	[3.0 HTML and Templating](#html-and-css)
	-	[3.1 HTML Basics](#html-basics)
		-	[3.1.1 What is HTML](#what-is-HTML)
		-	[3.1.2 Anatomy of an HTML Document](#anatomy-of-an-html-document)
		-	[3.1.3 An Overview of Common Tags](#an-overview-of-common-tags)
	-	[3.2 Templating in Flask](#templating-in-flask)
		-	[3.2.1 A Simple Example: hello.html](#a-simple-example-hello-html)
		-	[3.2.2 The Search Page](#the-search-page)
		-	[3.2.3 Template Variables](#template-variables-using-jinja)
		-	[3.2.4 Extending Templates](#extending-templates)
		-	[3.2.5 Extension: Templating Best-Practices](#templating-best-practices)
-	[4.0 CSS](#css)
	-	[4.1 CSS Basics](#css-basics)
		-	[4.1.1 Applying CSS Styles](#applying-css-styles)
		-	[4.1.2 Selectors](#selectors)
		-	[4.1.2 CSS Best Practices](#css-best-practices)
	-	[4.2 External Libraries](#external-libraries)
		-	[4.2.1 Installation and Template Setup](#installation-and-template-setup)
		-	[4.2.2 Using Foundation](#using-foundation)
		-	[4.2.3 Rewriting Templates](#rewriting-templates)

-------------------------

<a id="flask"></a>
# 1.0 Flask

Much of this tutorial is adapted from the [Flask website][flask].

<a href="#top" class="top" id="what-is-flask">Top</a>
## 1.1 What is Flask

[Flask][flask] is a Python microframework.  Microframeworks are bare-bones, customizable tools that make it easy to build web apps, and Flask lets us do this in Python.  It is very easy to setup and has excellent documentation on its [website][flask].

<a id="how-a-flask-app-works"></a>
### 1.1.1 How a Flask App Works

Flask works with a [client-server model][client-server].  The server, written in Python, has functions that take requests from clients (i.e. your web browser) and return web content to be displayed by the client.  

Think about it like a restaurant:  The patron (the client, or web browser) gets their meal (the web page) by telling it to the waiter (the Flask server).  Then, depending on the order (the request), the waiter gives it to the cook (back-end functions, optional) and then the server returns the cooked meal to the patron. 

In addition to serving static pages (meals off the menu), Flask servers have the ability of serving [dynamic web pages][dynamic-content], or pages that are generated every time you load the page (made to order).  For example, dynamic content could be of such pages include information stored in a database or a user account.

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
-	`requirements.txt` - A list of all of the dependencies for your project.  See more about dependencies and installing them in [section 6.3 of our Python tutorial](http://adicu.com/intro-webdev/python/#pip).
-	`static/` - This folder holds all your static files.  Static files include:
	-	`js/` - Javascript files, which allow interactive web content. We'll talk about these [later](#installation-and-template-setup).
	-	`css/` - CSS files, which style our app.  We'll talk about these [later](#css) too.
	-	`img/` - Image files.
-	`templates/` - This folder holds all your Flask templates.  Our HTML files will go here.  There are special features offered by Flask that make templates different than basic HTML files, explored in [Section 3.2](#templating-in-flask).

<a href="#top" class="top" id="hello-world-in-flask">Top</a>
## 1.2 Hello World in Flask

In order to write our first Flask app, we only need to edit one file: `app.py`.  It's that easy!

<a id="editing-app-py"></a>
### 1.2.1 Editing app.py

First, import the `Flask` class from the `flask` module.

```python
from flask import Flask
```

Then, construct the Flask `app` variable.  We'll pass around this variable whenever we want to access information about the server. We pass `__name__` into the `Flask()` function so that your flask app is associated with the directory structure we created in [Section 1.1](#the-anatomy-of-a-flask-app).

```python
app = Flask(__name__)
```

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

```bash
$ python app.py
```

If it's working, it should print the lines:

```bash
* Running on http://127.0.0.1:5000/
```

Point your browser to that URL and bask in the awesomeness!

> Wondering what that weird URL is?  `127.0.0.1` is the IP address for [localhost][localhost], or your local computer.  When we run a Flask server with `python app.py`, it is running only on your machine, not the internet.  The `:5000` bit is the [port][port], or specific place where your app is running.  Developing locally is much easier and safer than publishing your app to the internet every time you want to test something, and is considered good practice.  Also, instead of typing out `http://127.0.0.1:5000` every time you want to see your app, you can also point your browser to `http://localhost:5000`.  The two are equivalent.

<a id="developing-with-flask"></a>
### 1.2.3 Developing with Flask

Flask is great for development.  It offers very helpful error messages and prints stack traces well in the browser, if instructed to.  To enable these debugging features and (more importantly) automatic reload, edit `app.py` and add a statement configuring the `app` object.

```python
from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True  # Only include this while you are testing your app

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

With this modification, edit the string returned by the `hello()` function and refresh your browser to watch it change!  When you run the server now, it should also print:

	* Restarting on reloader

<a href="#top" class="top" id="working-with-routes">Top</a>
## 1.3 Working with Routes

Let's define a few more routes for our app. Again, [routes][route] are URLs that are supported by the server. We use the [decorator][decorators] `app.route()` to tie the decorated function to the URL given in the parenthesis.

<a id="static-routes"></a>
### 1.3.1 Static Routes

First, lets make a route that lets the client get the name of the creator of this app.  Start by defining a function called `name()`, and have it return your name as a string.


```python
def name():
  return "Your Name"
```

Now we'll apply the decorator `route()`.  Inside the parenthesis for the decorator, include the path `"/name"`.  Paths in Flask always start with a `/`.

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

Then, modify the `search` function to take a string variable `search_query`, and return that.

```python
@app.route("/search/<search_query>")
def search(search_query):
  return search_query
```

Save and reload your server as needed, and navigate to `http://localhost:5000/search/test` and see `test` appear as the returned page.  If you change what comes after the `/search/` in the URL, it will be displayed in the browser.  We will soon modify this route to return actual search results.

------------------------

<a id="apis"></a>
# 2.0 APIs

At this point, our server can handle searches to our system, but it doesn't do anything with them (it just spits them back out).  What we need next is to search Github for projects with the same keywords and return them to the client.  To do this, we will use Github's [API][api], or Application Programmer Interface.

<a href="#top" class="top" id="api-basics">Top</a>
## 2.1 API Basics

This section will take a step aside from our Flask project to build a foundation of knowledge around APIs and how they are used.  We will return to our app in [section 2.2](#the-github-search-api).

<a id="rest-apis"></a>
### 2.1.1 REST APIs

API's let us access external data in an easy, standardized way.  In the webapp world, when we say API we usually mean [REST (or RESTful) API][rest-api], which can be effectively thought of as an API that is accessible at a series of URL addresses. An extremely simple example of a REST API is [placekitten.com](http://placekitten.com), an API that serves images of kitten.  Here's how it works.  If you point your browser to `http://placekitten.com/<width>/<height>`, it returns a picture of a kitten with that width and height. If you go to `/g/<width>/<height>` the image will be grayscale.  Go to these urls to see a very basic REST API in action.

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
2.	The separator (`://`): A colon and two slashes always follow the protocol and are used to separate the protocol and the host.
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

```javascript
{ }
```

The core element of JSON documents are key-value pairs.  A key is a string, and a value can be (amongst other things) a string. Keys and values are separated by a colon (`:`).

```javascript
{ "name": "Jane Doe" }
```

Whitespace non-significant, and should be added for readability.

```javascript
{
	"name": "Jane Doe"
}
```

Multiple key-value pairs can be separated by commas (`,`).

```javascript
{
	"name": "Jane Doe",
	"occupation": "student",
	"school": "Columbia University"
}
```

Values can also be decimal numbers, boolean values (`true` or `false`), or `null`.

```javascript
{
	"name": "Jane Doe",
	"age": 20,
	"female": true,
	"male": false,
	"occupation": "student",
	"school": "Columbia SEAS",
	"children": null
}
```

Values can also be arrays.  Arrays are comma-separated values surrounded by brackets (`[ ]`).  Values in arrays should be all of the same type, but don't have to be.

```javascript
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
```

The final value type is the object.  An object is a set of comma-separated key-value pairs surrounded by braces (`{ }`).  In fact, our entire JSON document is one big object.

```javascript
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
```

> Most JSON documents are one big object, but they can also be one big array:
>
> <!--!!!javascript-->
> <!--!!!-->
> ```
> [
>     "This",
>     "Is",
>     {
>	      "valid": JSON
>	  }
> ]
> ```

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

```javascript
{"colors": [{"timestamp": 1187574833, "hex": "e0d1dd",
"id": 19425, "tags": 	[{"timestamp": 1111913422, "id":
11257, "name": "joyful"}, {"timestamp": 1108110854,
"id": 2798, "name": "lilac"}]}], "schemes": [],
"schemes_history": {}, "success": true, "colors_history":
{"e0d1dd": [{"d_count": 0, "id": "11257", "a_count": 1,
 "name": "joyful"}, {"d_count": 0, "id": "2798",
 "a_count": 1, "name": "lilac"}]}, "messages": [],
 "new_color": "e0d1dd"}
```

To view JSON in the browser, use a browser extension like JSONView ([Chrome][json-chrome], [Firefox][json-firefox]) or JSON Formatter ([Safari][json-safari]).  Install the appropriate extension and reload [that url](http://www.colr.org/json/color/e0d1dd).  You should now see the JSON with the proper indentation that we like.  If that didn't work for you or you're using another browser, copy the mess into [jsonprettyprint.com](http://jsonprettyprint.com/) to see it nicely formatted.

It should look like this:

```javascript
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
```

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

<a href="#top" class="top" id="the-github-search-api">Top</a>
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

The most basic way of interaction with an API call programmatically is through the command line.  The [cURL][curl] program runs in Terminal, and is used (most simply) to copy the content at a URL and print it to the screen.  First, open Terminal.  If you are on a Mac, open Finder, click `Applications` on the sidebar, open the `Utilities` folder, and then double click `Terminal`.

Change directory into your *working directory*, or the directory where `app.py` is.

Type the following command:

```bash
$ curl https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5+language:JavaScript
```

You should see the entire JSON response (probably pretty long!) print to the console.  Now lets write that response to a file:

```bash
$ curl https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5+language:JavaScript > response.json
```

> The `> response.json` section redirects all the output that would normally be sent to the console into the `response.json` file.

You should now have a new file in your current directory named `response.json`.  If you open that file in your text editor, you'll see the response!

<a id="using-python"></a>
### 2.2.3 Using Python

Python has several built in libraries for handling REST APIs, but the external library [Requests][py-requests].  To install it, use [Pip][pip]:

```bash
$ pip install requests
```

Don't forget to update your `requirements.txt` file to reflect this change!

Create a new python file:

```bash
$ touch github.py
```

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

```bash
$ python github.py
<Response [200]>
```
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

Addressing the first issue is simple.  We'll let the `url` string be the base search URL concatenated with the `search_query` variable. Don't forget to import `requests`!

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

Write a function called `parse_response()` that takes in `response_dict` and returns a cleaned up dictionary that maintains the structure of `response_dict` but only has the keys enumerated above.  Pass `response_dict` through this function before calling `jsonify()` on it.  When you run your program, you should see a cleaner JSON output.

<a id="using-javascript"></a>
### 2.2.6 Extension: Using JavaScript

*If you're familiar with JavaScript and would prefer to interact with the GitHub API using JavaScript, we'll go over how
to do that in this section. If you don't know JavaScript, feel free to skip it.*

Vanilla JavaScript has a way to interact with external APIs, but [jQuery](http://jquery.com/), a library of common
functions that simplifies your JavaScript, makes everything much easier. To include it, put the following lines into a new file called `js_test.html` in your working directory:

    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
    <script src="script.js"></script>
    <p>Open the JavaScript Console!</p>

After this is run, jQuery will be bound to the `$` object. All calls beginning with `$` are jQuery-related.

jQuery makes selecting DOM elements (that is, the HTML elements on your web page) incredibly simple using
[selectors](http://api.jquery.com/category/selectors/): to "select" all of the `img` elements on your page, do
`$("img")`; to select an element with id `example-id`, do `$("#example-id")`. Once an element is selected, you can
perform a number of actions with it; a fun one is `.fadeOut()`. See more at the
[jQuery API Documentation](http://api.jquery.com/).

jQuery also lets you perform *AJAX* (Asynchronous JavaScript and XML) requests easily. This is a mechanism that your
JavaScript can use to fetch new data without loading a new page (it's how your GMail inbox knows you have a new message
without you refreshing the page). Create another file called `script.js` with the following lines:

```javascript
$.getJSON("https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5+language:JavaScript&callback=?", function(data) {
	console.log(data);
});
```

Here (as before), we fetch all repositories that match the string "Space Invaders" and are written in JavaScript; we
then print it out to the JavaScript console (which can be accessed in the "Developer Tools" for Firefox (`Ctrl-Shift-K`)
or Chrome (`Ctrl-Shift-J`) (or `Cmd` for OS X).

Open up `test_js.html` in your browser and see the response from your JSON request in the JavaScript Console.

A couple of gotchas here:

* We add the parameter `callback=?`; this is a [JSONP](https://en.wikipedia.org/wiki/JSONP) callback to get around the
  [same-origin policy](https://en.wikipedia.org/wiki/Same-origin_policy). It's necessary for security reasons; for more
  information, see those links.

* We process the data in a *callback* (that's the `function(data) { ... }` bit). This is because loading data over the
  internet takes time; rather than stop everything up while we're waiting for that to finish, JavaScript moves on and
  executes the next statement. We tell JavaScript what we want it to do once it's finished loading the data; that's the
  body of the function we pass to `getJSON`.

That's it! You've successfully queried GitHub's API using JavaScript and jQuery.

<a href="#top" class="top" id="authentication">Top</a>
## 2.3 Extension: Authentication

If you refresh your web browser enough times, you may see the expected JSON disappear and be replaced by an error message.
After about 5 requests you should get a rate limiting error.
Included is [this link][github-rate-limiting] which details how github does rate limiting.
For the [search-api][github-search-rate-limiting] we're locked out after 5 requests/minute because we have not authenticated with GitHub.
Once we authenticate we'll be able to do 20 requests/minute.

<a id="basic-authentication"></a>
### 2.3.1 Extension: Basic Authentication

To authenticate with GitHub, we'll check out [their documentation][github-new-token] on creating a reusable token.
Getting a token allows us to have reusable credentials to GitHub's API without saving our credentials in plain-text.
The endpoint given is `https://api.github.com/authorizations`, it implements [Basic HTTP Authentication][basic-http-auth]. 
We can test the request using [curl][curl].
We won't give the token any [scopes][github-token-scopes] since we will be using it for the search API.

```bash
$ curl -X POST \        # the -X flag declares what kind of HTTP request we are making
  -u <username> \       # the -u flag allows us to pass our username for the Basic HTTP Auth
  -d '{"scopes": []}' \ # the -d flag passes data for the post request
  https://api.github.com/authorizations
Enter host password for user '<username>'

{
  "id": 5188246,
  "url": "https://api.github.com/authorizations/5188246",
  "app": {
    "name": "GitHub API",
    "url": "http://developer.github.com/v3/oauth/#oauth-authorizations-api",
    "client_id": "00000000000000000000"
  },
  "token": "<YOUR TOKEN HERE>",
  "note": null,
  "note_url": null,
  "created_at": "2014-01-10T08:02:44Z",
  "updated_at": "2014-01-10T08:02:44Z",
  "scopes": [
  ]
}
# the second step can be skipped
$ curl -X POST -u <username>:<password> -d '{"scopes": []}' https://api.github.com/authorizations
{
  ...
}
```

Now we'll try to do this in Python.
The [requests library makes HTTP Basic Auth][py-requests-basic-auth] very straightforward.

```python
import requests
import json

gh_username = raw_input('GitHub username: ')
gh_password = raw_input('GitHub password: ')
payload = json.dumps({'scopes': []})

gh_response = requests.post('https://api.github.com/user', auth=(gh_username, gh_password), data=payload)
print gh_response.json()['token']
```

This example will return a new token linked to your account.
Adding the token to your parameters will change the rate that GitHub imposes to 20 requests/minute.

Try adding this authentication to your app.
Generate a GitHub token using the script, add this token to a bash settings file.
Add the token to your app config on startup.
Pass the token [as a parameter][github-token-auth] for each request.

-------------------------

<a id="html-and-css"></a>
# 3.0 HTML and Templating

We've done some really exciting work already, displaying JSON content in all sorts of different ways, and even creating dynamic routes in Flask that return different content based on what URL you visit.  

For our web app, we want more than this, however.  We will display not just the raw JSON content, but a user-friendly search experience and an attractive results page.  To do this, we will use [HTML](#html-basics) and [Flask's templates](#templating-in-flask).

<a href="#top" class="top" id="html-basics">Top</a>
## 3.1 HTML Basics

<a id="what-is-HTML"></a>
### 3.1.1 What is HTML

[HTML][html], or HyperText Markup Language is the main lanugage we use for creating content that will be displayed by a browser.  So what is HTML?  Well, at the very core, it's text.  Create a file in your working directory, and call it `hello.html`.  Inside it, just type:

```html
Hello World!
```

No funny business, just the two words.  If you open `hello.html` in your browser, you'll see it display `Hello World!`.  Congratulations on writing your first HTML document! Every text document can be interpreted as an HTML document (just add the `.html` extension!), but true HTML documents organize themselves in a structured way, using *elements*.

##### Elements

Elements are made up of the *start tag*, the *content*, and the *end tag* (or *closing tag*). Both the start and end tags are wrapped in angle brackets (`< >`), and contain the element name inside them.  The end tag has slash (`/`) that immediately follows the open angle bracket.  Content of elements can be plain text, or even more HTML. Copy this example element into `hello.html`, and view it in your browser:

```html
Hello World!

<p>This is a really cool paragraph</p>
```

The start tag is `<p>`, the content is `This is a really cool paragraph`, and the end tag is `</p>`.  The element name in this case is `p`, for paragraph.  Because the content of an element can be HTML, we can nest tags inside each other.  So for example, if we wanted to **em**phasize that the paragraph is cool, we could wrap the words "really cool" in `<em>` tags, like this:

```html
Hello World!
<p>This is a <em>really cool</em> paragraph</p>
```

Reload `hello.html`.  You'll probably see the words "really cool" italics.  Now lets say we want to put even **strong**er emphasis on the word "really". We can use the `<strong>` tag for that.  Edit `hello.html`:

```html
Hello World!
<p>This is a <em><strong>really</strong> cool</em> paragraph</p>
```

If you reaload `hello.html`, you should see that "really cool" is in italics, and "really" is also in bold.  Does that mean the the `<em>` is used to make words italic and `<strong>` is used to make them bold?  No.  Most web browsers have agreed that emphasis should be expressed using italics, and strong emphasis should be expressed with bold font, but as writers of HTML, we use tags to describe the purpose of the content, not to acheive the format that we see once they're applied.

##### Headings

One rule of thumb for writing good HTML:  All text should be wrapped in tags, and the tags should be meaningful.  Right now, our `Hello World!` text has no tags around it, so let's figure out what tag makes the most sense.  "Hello World!" is the title of our `hello.html` web page, so we'll use the heading tags to indicate this.  The `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, and `<h6>` tags are used for headings and subheadings, `<h1>` being the highest level (and usually the largest), and `<h6>` being the lowest level (and usually the smallest).  Let's wrap our page title in `<h1>` tags.

```html
<h1>Hello World!</h1>
<p>This is a <em><strong>really</strong> cool</em> paragraph</p>
```

Reload `hello.html` and see the `<h1>` tag in action!  You might have an instinct to mess around with the different headings 1-6, and you should go ahead!  But remember this, we chose `<h1>` because "Hello World!" was the title of our webpage, not because we wanted it to be large.  So as you switch the `<h1>` tags to `<h2>`, remember that it wouldn't really make any sense to include an `<h2>` element in a website without an `<h1>` element, because that would mean a subheading without a heading.  From `<h2>` and down, headings should be interchanged depending on their importance.

##### Attributes

HTML elements can also have [attributes][attributes].  Attributes are key-value pairs that modify the contents of HTML elements, or provide additional information about the element itself.  For example, when we use the `<a>` tag to create an **a**nchor, or hyperlink, we have to provide the desitination in the `href` attribute.  Edit `hello.html`:

```html
<h1>Hello World!</h1>
<p>This is a <em><strong>really</strong> cool</em> paragraph.  My favorite search engine is <a href="http://www.google.com">Google</a></p>
```

The `href` is the key, and then we set it `=` to the value `"http://www.google.com"`.  If you reload `hello.html`, you'll see a blue (or maybe purple), underlined link to google.com on your page!

> Wondering what "href" stands for?  So do we.  It's extremely unclear in the community, and while there is some consensus that it *should* mean "**H**ypertext **REF**erence", there is still [confusion][href-confusion].

<a id="anatomy-of-an-html-document"></a>
### 3.1.2 Anatomy of an HTML Document

The purpose of HTML documents is to provide a semantic structure that represents the web page that is being displayed.  When talking about HTML, semantic means that all the tags are used for the appropriate purposes, and that all necessary information is included in the HTML source code.

In this section, we'll dissect a boilerplate HTML document that follows HTML5 (the most modern) standards that help ensure that your HTML is rendered as best as possible by all devices and browsers. Here is the document:

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>My Website</title>
	</head>
	<body>
		<!--Page content-->
	</body>
</html>
```

The first line is the our file's [doctype][doctype].  according to the HTML specification, the doctype is a "required preamble", but for our purposes, it's just something you should always include.  

> Wondering how we got away with writing an HTML document without a DOCTYPE, or think you're too cool for one?  Read this [stack overflow response](http://stackoverflow.com/a/7695075) that summarizes it pretty well.  Use it, or be prepared to feel the pain that may or may not eventually result from such hubris. 

Older HTML standards include a much wordier DOCTYPE tag at the beginning of the document, but we only need:

```html
<!DOCTYPE html>
```

Note that this is not an element, and is just a tag.  There is an `!` at the beginning of it and there is no closing tag.  This is one of the only cases where this will be true.

Next, we see the line:

```html
<html lang="en">
```

This the the opening tag of the `<html>` element.  You can see it's closing tag at the last line.  We use the `<html>` element as the root for all other elements, by convention.  The `lang` attribute is used to indicate that the primary language for this document will be English.

Moving inwards to the *children* of the `<html>` element, or elements one level within it, we see the `<head>` and `<body>` elements.  

The `<head>` element holds all the information about the web page that should not be displayed within the browser window.  The `<body>` tag holds all the elements that should be displayed.  

Within the `<head>` element, we first have a `<meta>` element:

```html
<meta charset="utf-8">
```

The `<meta>` element does not have content or a closing tag, tells us extra information about this document.  By default, we indicate that our character set will be `utf-8`, or unicode.

The next line is more straightforward.

```html
<title>My Website</title>
```

The `<title>` element tells the browser the name of our website.  If you load this example in your browser, you'll see `My Website` show up as the title of the page (even though it will have no content in the browser window).

Within the `<body>` element, all we have is the line:

```html
<!--Page content-->
```

Everything wrapped between the `<!--` and the `-->` is a comment, and won't show up in the page.  Edit `hello.html` to reflect the standard HTML5 template.  We can remove the comment.

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>Hello World!</title>
	</head>
	<body>
		<h1>Hello World!</h1>
		<p>This is a <em><strong>really</strong> cool</em> paragraph.  My favorite search engine is <a href="http://www.google.com">Google</a></p>
	</body>
</html>
```

When you reload `hello.html`, you may not notice any change.  However, constructing our document in this manner will make it more extensible and cross-device compatible.

<a id="an-overview-of-common-tags"></a>
### 3.1.3 An Overview of Common Tags

There are many HTML elements that you will use for your website.  There are some basics you should know, before you dive into it, however.  Most of this section is summarized from the [Mozilla Developer Network (MDN)][mdn], more specifically their [HTML element reference][mdn-elements].  

**DO NOT SKIM THIS NEXT PARAGRAPH**

Please, please, please use MDN.  There is another site, called W3 schools (hyperlink intentionally excluded) that consitently turns up higher in Google search rankings, and consistently has incorrect, outdated, and more confusing information on the same topics.  If you have a question about web development (generally HTML, CSS, or JavaScript), just append "mdn" to the end of your search, to make sure that you get MDN as the top result.  The team at Mozilla has done an excellent job of making an excellent website that has the most up-to-date information about good web development practices. 

##### Structure
-   `<html>` [(MDN)][mdn-html] - All HTML should be wrapped in the `<html>` element.  It should be the only element at the top level of an HTML document (except `<DOCTYPE>`).
-   `<body>` [(MDN)][mdn-body] - Represents the content of the HTML document.  All visible elements are descendant from the `<body>` tag.
-   `<head>` [(MDN)][mdn-head] - Holds all the metadata about the document.  This could include the title, charset, styling, and scripts
-   `<div>` [(MDN)][mdn-div] - A general purpose container, to be used when no other element has semantic meaning.  Using [CSS](#css), `<div>` elements can be made to server all sorts of stylistic purposes.  There are [a lot of elements][mdn-elements] to choose from, so be sure that nothing else fits before using a `<div>`.  That said, you will find that you end up using `<div>` elements with some frequency.
-   `<span>` [(MDN)][mdn-span] - Another general purpose container, but specifically for inline content.  For example, if you want to highlight misspelled words in a page, wrapping them in a span that has been configured to highlight its content would be the best solution.  Don't use a `<div>` when a `<span>` would be more appropriate.

##### Text
-   `<p>` [(MDN)][mdn-p] - A paragraph of text.  
-   `<a>` [(MDN)][mdn-a] - A link, or anchor.  Be sure to always include the `href` attribute when using `<a>` tags.  If a link doesn't go anywhere, set the `href` attribute equal to `"#"`.
-   `<h1> - <h6>` [(MDN)][mdn-h1-6] - Headers of various levels, `<h1>` being the highest level (like the title of an article or the title of the page), and `<h6>` being the most low level heading.  For [Search Engine Optimization (SEO)][seo] reasons, you should only include on `<h1>` tag on every page.
-   `<em>` [(MDN)][mdn-em] - Emphasis.  While on many browsers this will make text italic, do not use `<em>` elements for only this purpose.  Only use emphasis tags when words need emphasis.
-   `<strong>` [(MDN)][mdn-strong] - Strong emphasis.  Usage rules are similar for the `<em>` element.
-   `<br>` [(MDN)][mdn-br] - For line breaks.  Using `<br>` tags is only really appropriate when writing a poem, address, or something else where line breakage is important.  Don't use this for the space between two paragraphs (just use two `<p>` tags!).

##### Lists
-   `<ol>` [(MDN)][mdn-ol] - An ordered list.  Ordered lists should only contain list items (`<li>` elements).  Only use an `<ol>` when the order of the items in the list matters, like a recipe or instructions.
-   `<ul>` [(MDN)][mdn-ul] - An unordered list.  Unordered lists should also only contain list items (`<li>` elements).  Use this when you have a list of similar items, but the order does not matter.  
-   `<li>` [(MDN)][mdn-li] - An item in a `<ul>` or an `<ol>`.

##### Forms
-   `<form>` [(MDN)][mdn-form] - A wrapper for any form that the user will fill out on the page. If you are making a web form, check out [this instructional guide][mdn-form-usage] from MDN on how to build a basic form.
-   `<input>` [(MDN)][mdn-input] - An element that is used to input data into a form.  This could be a text-box, radio button, or an email address box depending on the attributes used.  Input tags are self closing, meaning that they don't have content or an end tag, and just take the form `<input />`.
-   `<label>` [(MDN)][mdn-label] - A piece of text that labels an input.
-   `<textarea>` [(MDN)][mdn-textarea] - A large, multiline text box that is part of a form.
-   `<button>` [(MDN)][mdn-button] - Used for a button that submits or resets the form.

##### Meta / Informational

Except the `<DOCTYPE>` tag, all of these elements should be children of the `<head>`.

-   `<DOCTYPE>` [(MDN)][mdn-DOCTYPE] - The declaration of the document type.
-   `<meta>` [(MDN)][mdn-meta] - Provides extra information about the document.  The `<meta`> tag may serve a bunch of different purposes depending on its attributes.
-   `<link>` [(MDN)][mdn-link] - Linking this document to an external resource.  For the most part, the `<link>` tag is only used for linking to an external CSS file.  We'll learn more about this syntax in [section 4.1](#css-basics).  Be sure to always include the `href`, `rel`, `type`, and `media` attributes, as follows: 
```html
<link href="style.css" rel="stylesheet" type="text/css" media="all">
```
-   `<style>` [(MDN)][mdn-style] - Embedded CSS style.  While it is better practice to use `<link>` to an external CSS file, it is also possible to include CSS content in a `<style>` element.
-   `<title>` [(MDN)][mdn-title] - The title of your page.

##### Other

-   `<img>` [(MDN)][mdn-img] - Used to include an image on the page.  Always include the `src` attribute, the URL of the image resource, and the `alt` attribute to describe the image if for some reason the image cannot or should not be loaded.  The `<img>` element is self closing, like the `<input>` element.  We write it in the form `<img />`.  For example:
```html
<img src="https://developer.cdn.mozilla.net/media/img/mdn-logo-sm.png" alt="MD Logo" />
```
-   `<script>` [(MDN)][mdn-script] - Use to either embed JavaScript (in rare occasions) or link to external JavaScript file (more common).  Always include the `type` attribute, and include the `src` attribute if the file is external.  Here is an example of the two different styles of using the `<script>` element:
```html
<script type="text/javascript" src="my_script.js"></script>
<script type="text/javascript">
	console.log('Hello Console!');
	alert('Hello World!');
</script>
```

<a href="#top" class="top" id="templating-in-flask">Top</a>
## 3.2 Templating in Flask

At the most basic level, templates in Flask are HTML documents in the `templates` folder of our project directory.  These HTML documents can have some added features, however.

<a id="a-simple-example-hello-html"></a>
### 3.2.1 A Simple Example: hello.html

Let's make our Flask app return `hello.html` as a template.  First,  move `hello.html` into the `templates` folder.  Then, in `app.py`, import `render_template` from the `flask` package:

```python
from flask import Flask, jsonify, render_template
import requests
...
```

The function `render_template()` turns templates in your `templates` folder into HTML that can be sent to the client.  For simple templates like `hello.html`, this method won't do more than just copy it into one big unicode string.

Now for our `/` route, we'll return the string that is created by calling `render_template()` on the name of the template file.

```python
...
@app.route("/")
def hello():
    return render_template("hello.html")
...
```

Reload the server and visit `localhost:5000`.  You'll see `hello.html`, but this time rendered by Flask!

<a id="the-search-page"></a>
### 3.2.2 The Search Page

Let's write an interface for users to search in HTML.

First start by creating a template called `search.html` in the `templates` folder.  Copy in the boilerplate from [section 3.1.2](#anatomy-of-an-html-document) into this file, changing the title of the page to `Search`.

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>Search</title>
	</head>
	<body>
		<!--Page content-->
	</body>
</html>
```

The first thing we should do is add a title to the search page. We'll use `<h1>` because this will be the top level heading.

```html
...
<body>
	<h1>Search</h1>
</body>
...
```

Now, lets create a web form, that allows users to enter a search query and click search.  We'll make a very simple search form (following guidelines from [MDN][mdn-form-usage]).  Start with a `<form>` element.  We fill out the `action` and `method` attributes in accordance with HTML5 standards.

```html
...
<h1>Search</h1>
<form action="/search" method="post">
</form>
...
```

Next we'll add an `<input>` method with `type` attribute equal to `text`, in order to make a text field.  We'll add placeholder text using the `placeholder` attribute, to cue in users as to how to use the form.  We also include the `name` attribute, which lets us standardize how the data from the form will be sent to our Flask server.  Finally, add the attribute `required` (it does not take a value).  This ensures that we don't submit the form when the text box is empty.

```html
...
<form action="/search" method="post">
	<input type="text" placeholder="Search for your idea" name="user_search" required/>
</form>
...
```

Then we'll add a search `<button>`:

```html
...
<form action="/search" method="post">
	<input type="text" placeholder="Search for your idea" name="user_search" required/>
	<button type="submit">Search</button>
</form>
...
```

Now we have our completed `search.html`:

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>Search</title>
	</head>
	<body>
		<h1>Search</h1>
		<form action="/search" method="post">
			<input type="text" placeholder="Search for your idea" name="user_search" required/>
			<button type="submit">Search</button>
		</form>
	</body>
</html>
```

When the user clicks our `<button>`, a [POST request](#http) will be sent to our `/search` route, with the data from the form being passed in the POST request body (user_search=my-idea). We will have to *refactor*, or rewrite our `search()` method to take data this way, and to display the template if no data is provided.

To account for the data coming in as a parameter in the request body, we'll change the route from `/search/<search-query>` to `/search` and remove the parameter from the method.  Edit `app.py`:

```python
...
@app.route("/search")
def search():
...
```

Now we'll either return `search.html` or the JSON data depending on the method that was used: `GET` if the user visits `localhost:5000/search` in their browser, and `POST` if they click submit on the form.  

By default, Flask routes only accept `GET` requests, but we can change this by modifiing the `route()` decorator:

```python
...
@app.route("/search", methods=["GET", "POST"])
...
```

In order to figure out which method was used, we need to import `request` from the `flask` package (not to be confused with the external library `requests` that we imported in [section 2.2.3](#using-python)):

```python
from flask import Flask, jsonify, render_template, request
import requests
...
```

Now, in every route there is an associated `request` that has lots of data from the HTTP request that was sent to the server, including the method and the args (from the query string!).  Edit the `search()` method:

```python
...
@app.route("/search")
def search():
    if request.method == "POST":
        url = "https://api.github.com/search/repositories?q=" + request.form["user_search"]
		response_dict = requests.get(url).json()
		return jsonify(response_dict)
    else: # request.method == "GET"
        return render_template("search.html")
...
```

Note that `request.form` is a [multidict][multidict], and we can get the search data from the `user_search` key, because `user_search` is the `name` attribute of the `<input>` element in our HTML form.  

Now if you go to `localhost:5000/search` you will see the form, and if you submit data with the form, you will see the JSON data.  All with one `/search` route!

<a id="template-variables-using-jinja2"></a>
### 3.2.3 Template Variables Using Jinja2

Now displaying data as JSON is all well and good, but it would be great to display the content as HTML.  The problem is, we can't know at the point of writing our HTML what the response will be, so we'll use the more advanced templating features of Flask to dynamically create HTML.

We'll be using the [Jinja2 templating engine][jinja2] built into Flask. Using it, we can pass variables from our Python code into templates, essentially allowing us to incorporate variables in our HTML.

First, create a boilerplate HTML5 document called `results.html`:

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>Results</title>
	</head>
	<body>
		
	</body>
</html>
```

Before we can start designing our template, we have to actually pass the variable into the template.  We do this in the `render_template()` function, where ([as the documentation indicates][render-template]) we can pass variables as keyword arguments.  We can also remove our import for jsonify, as we are no longer using it.  Edit `app.py`:

```python
from flask import Flask, render_template, request
import requests
...
		response_dict = requests.get(url).json()
		return render_template("results.html", api_data=response_dict)
...
```

> Here the variable `api_data` has an arbitrary name chosen to be used from within the template.  Inside the template, we will refer the the data as `api_data`, not `response_dict`.  Often these two names will be the same, i.e. `response_dict=response_dict`, but we'll leave them different for clarity.

We've passed our data into the HTML document, so now we'll turn `results.html` into a dynamic template.  As a concept, lets have an unordered list of all the results, where each item represents a repository with its name, description, and author's username. 

First, create an unordered list for the results.

```html
...
<body>
	<ul>
	</ul>
</body>
...
```

Next, we'll iterate over all of the repositories in the `items` list using Jinja2's [for loop syntax][jinja2-for], making a list item for each one.  We know to do this because of the JSON response structure we saw in section [2.1.4](#viewing-json-in-the-browser).  When `render_template()` is called on this template, Flask will replace the for loop with mulitple instances of whatever is inside the `{%%}` tags.  

In general, Jinja2 code that contains `{%%}` is for control flow, and will not be displayed literally on the web page.

```html
...
<body>
	<ul>
	{% for repo in api_data["items"] %}
		<li></li>
	{% endfor %}
	</ul>
</body>
...
```

Now lets populate the dynamic list item.  We can insert variables into Flask using the `{{ variable }}` syntax.

```html
...
<ul>
{% for repo in api_data["items"] %}
	<li>
		<h3>{{ repo.name }} by {{ repo.owner.login }}</h3>
		<p>{{ repo.description }}</p>
	</li>
{% endfor %}
</ul>
...
```

Now, visting `localhost:5000/search` again and submit a search. You should see a bulleted list of results for your search!

<a id="extending-templates"></a>
### 3.2.4 Extending Templates

Our results page looks great, but what if we want to do another search?  Let's put the search form and header at the top of `results.html` as well.

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>Results</title>
	</head>
	<body>
		<h1>Search</h1>
		<form action="/search" method="POST">
			<input type="text" placeholder="Search for your idea" id="user_search" name="user_search" required/>
			<button type="submit">Search</button>
		</form>
		<ul>
		{% for repo in api_data["items"] %}
			<li>
				<h3>{{ repo.name }} by {{ repo.owner.login }}</h3>
				<p>{{ repo.description }}</p>
			</li>
		{% endfor %}
		</ul>
	</body>
</html>
```

Noticing a lot of repeated code? You should.  `search.html` and `results.html` look very similar, and it would be great if we didn't have to reuse code.  

We can use *template inheritance* to reuse one template with another.  It's easy!  The *parent template* will be `search.html`, because it is more simple, and all of the code from it shows up in `results.html`.  In `search.html`, add a [Jinja2 block][jinja2-block] that the child (`results.html`) will fill in:

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>Search</title>
	</head>
	<body>
		<h1>Search</h1>
		<form action="/search" method="POST">
			<input type="text" placeholder="Search for your idea" id="user_search" name="user_search" required/>
			<button type="submit">Search</button>
		</form>
		{% block results %}{% endblock %}
	</body>
</html>
```

Next, we'll make `results.html` *extend*, or be a child of `search.html`.  To do this, add the following line at the beginning of `results.html`:

```html
{% extends search.html %}
<!DOCTYPE html>
```

Now, we can delete everything that is in `search.html` from `results.html`, and just include the contents of our `{% block %}`.  Edit `results.html`:

```html
{% extends "search.html" %}
{% block results %}
<ul>
{% for repo in api_data["items"] %}
	<li>
		<h3>{{ repo.name }} by {{ repo.owner.login }}</h3>
		<p>{{ repo.description }}</p>
	</li>
{% endfor %}
</ul>
{% endblock %}
```

And that's it!  When `render_template()` is called on `results.html`, Flask sees that `results.html` extends `search.html`, so it renders `search.html` filling in any `{% block %}`s that were define in `results.html`.  When `search.html` is rendered, the empty `{% block %}` is ignored.  

View it live!  You'll see the form persist into the results page, even though `results.html` doesn't have the form HTML in it.

<a id="templating-best-practices"></a>
### 3.2.5 Extension: Templating Best-Practices

Our `results.html` template works, but there are some corner cases that we'd be good to cover.  We'll be addressing some issues with the user experience of our app.  Figuring out that you have user experience problems can be hard to do, but as a rule of thumb, give your app to a few friends and see what they think after using it.

##### Empty search results

What if there are no results from the search?  The `items` list will be empty, and no `<li>` elements will be rendered.  Lets have a fall back.  Using the `{% if %}` control statement, we can check if the `items` list exists and isn't empty, and display a message indicating a lack of results otherwise.

```html
{% extends "search.html" %}
{% block results %}
{% if api_data["items"] %}
	<ul>
	{% for repo in api_data["items"] %}
		<li>
			<h3>{{ repo.name }} by {{ repo.owner.login }}</h3>
			<p>{{ repo.description }}</p>
		</li>
	{% endfor %}
	</ul>
{% else %}
<p>There are no results found on Github.  Your idea is original!</p>
{% endif %}
{% endblock %}
```

##### Missing Data Members

What if a project doesn't have a description?  Or the name / creator data is corrupted?  Whenever we use template variables, we should be sure that they exist first, lest the user see some ugly template error instead of your app.

Wrap each `{{ }}` statement in a Jinja2 `{% if %}`, checking if the variable exists before using it.  Here are some general rules for our case:

-   The entire list item should be omitted if there is no `repo.name`.
-   The ` by ` and the owner should be omitted if there is no `repo.owner.login`.
-   The entire `<p>` element should be omitted if there is no `repo.description`.

Make these fixes.

------------------------

<a id="css"></a>
# 4.0 CSS

[CSS][css], or Cascading Style Sheets, is a styling language that is used to arrange and stylize HTML elements.  CSS is extremely powerful, but also fairly hard to learn.  Every different browser interprets CSS slightly differently, and there are a lot of tricks and best practices that are hard to learn.  As such, CSS is best learned by lots and lots of practice.  The [ADI Resources][learn] page has links to a lot of different tutorials and walkthroughs, if you want more practice after styling your Flask app.

<a href="#top" class="top" id="css-basics">Top</a>
## 4.1 CSS Basics

CSS is a very simple language.  At it's core, CSS is made up of three parts: *selectors*, *properties*, and *values*.  Selectors (explored in depth in [section 4.1.2](#advanced-selectors)) are used to select which elements are being styled.  For example:

```css
p { }
```

selects all `<p>` elements.

Inside the braces `{ }` are the *properties* and *values* separated by colons `:`, with semicolons `;` at the end of each property / value pair.  For example:

```css
p { color: blue; }
```

would make all the `<p>` tags blue. Here, `color` is a property and `blue` is a value.  In terms of syntax, that's really it.  If we wanted to make all `<p>` tags blue and all `<strong>` tags red, here would be our CSS:

```css
p {
	color: blue;
}
strong {
	color: red;
}
```

Notice that whitespace is not relevant to syntax.  Finally, comments should be surrounded in `/* */`.

```css
/* this is a comment */
```

There is an extremely large collection of CSS properties and values, all of which are documented excellently at (surprise) the [Mozilla Developer Network][mdn].  Again, avoid incorrect or out of date information by appending `mdn` to any Google searches related to CSS you might have!

<a id=""></a>
### 4.1.1 Applying CSS Styles

There are three ways to apply CSS to HTML elements.  The first is called *inline styling*.  Every element can be given a `style` attribute that can take CSS styles that apply to this element.  Doing this, we can avoid selectors entirely because all of our styling effects only the element that we are adding the `style` attribute to.  For example, this `<p>` tag will have blue text:

```html
<p style="color: blue">This text is blue.</p>
```

Inline styles are problematic, however.  Not only do we clutter the text that is being displayed, but also we would have to duplicate our styling for every paragraph we have!

```html
<p style="color: blue">This text is blue.</p>
<p style="color: blue">An so is this text.</p>
<p style="color: blue">And this text.</p>
```

Because of this, inline styles should be *absolutely avoided* unless you are writing for mail clients that ignore CSS that isn't inline.

We can also apply CSS in a `<style>` element, in the `<head>`, like so:

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>CSS Demo</title>
		<style>
p {
	color: blue;
}
		</style>
	</head>
	<body>
		<p>This text is blue.</p>
		<p>An so is this text.</p>
		<p>And this text.</p>
	</body>
</html>
```

This is great, because the body of the document is a lot less cluttered.  As you can imagine, this is only relocates the problem.  now the head of the document is messy and full of CSS styles.  As your HTML gets longer so does your CSS, and now documents can reach unmanageable length.

For the same reason we might break up a large programming project into classes and functions, we want to get our CSS out of our `.html` document entirely.  Enter the `<link>` tag, which lets us reference external `.css` stylesheets!  Link tags only need an open tag, and have no content or end tag.  Also, be sure to always include the `rel` attribute as 'stylesheet' and the `type` attribute as `text/css` alongside the `href` attribute pointing to the `.css` file.

<h1 class="join"></h1>
```html
<!DOCTYPE html>
<!-- demo.html -->
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>CSS Demo</title>
		<link src="demo.css" 
			rel="stylesheet"
			type="text/css">
	</head>
	<body>
		<p>This text is blue.</p>
		<p>An so is this text.</p>
		<p>And this text.</p>
	</body>
</html>
```
```css
/* demo.css */
p {
	color: blue;
}
```
<h1 class="clear"></h1>

Using an external CSS file is the best practice, barring special circumstances.  You can even include multiple CSS files to keep things organized.

```html
<!DOCTYPE html>
<!-- demo.html -->
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>CSS Demo</title>
		<link href="blue.css" rel="stylesheet" type="text/css">
		<link href="red.css" rel="stylesheet" type="text/css">
	</head>
	<body>
		<p>This text is blue.</p>
		<strong>And this text is red.</strong>
	</body>
</html>
```

<h1 class="join"></h1>
```css
/* blue.css */
p {
	color: blue;
}
```
```css
/* red.css */
strong {
	color: red;
}
```
<h1 class="clear"></h1>

<a id="selectors"></a>
### 4.1.2 Selectors

In the above examples `p` and `strong` in the `.css` files are *selectors*.  Selection can be done in a variety of different ways.  The most basic selection is by element name.

<h1 class="join"></h1>
```html
<!-- demo-name.html -->
<p>This text is blue</p>
<strong>This text is not</strong>
```
```css
/* demo-name.css */
p {
	color: blue;
}
```
<h1 class="clear"></h1>

If you provide a `class` attribute, the `.classname` syntax will select all elements with `class="classname"`.  Elements can have multiple classes using the syntax `class="classname1 classname2"`.

<h1 class="join"></h1>
```html
<!-- demo-class.html -->
<p class="blue">This text is blue</p>
<p>This text is not blue</p>
<p class="blue underline">
	This text is blue and underlined.
</p>
```
```css
/* demo-class.css */
.blue {
	color: blue;
}
.underline {
	/* Use the "text-decoration"
	property to underline text. */
	text-decoration: underline;
}
```
<h1 class="clear"></h1>

You can also give an element a unique `id` and it can be selected with the `#idname` syntax.  Do not give two elements the same id.

<h1 class="join"></h1>
```html
<!-- demo-id.html -->
<p id="blue">This text is blue</p>
<p>This text is not blue</p>
```
```css
/* demo-id.css */
#blue {
	color: blue;
}
```
<h1 class="clear"></h1>

There are also *relational selectors* for finding elements in the HTML document.  

Using the *descendant* selector syntax, or `selector1 selector2`, you can restrict `selector2` to only elements that are descendants of an element selected by `selector1`. For example:

<h1 class="join"></h1>
```html
<!-- demo-descendant.html -->
<div class="blue">
	<h1>This text is not blue</h1>
	<p>This text is blue</p>
	<span>
		<p>This text is also blue</p>
	</span>
</div>
<p>This text is not blue</p>
```
```css
/* demo-descendant.css */
.blue p {
	color: blue;
}
```
<h1 class="clear"></h1>

Similarly, the child selector syntax (`selector1 > selector2`) will restrict `selector2` to only children (not grandchildren or other descendants) of elements selected by `selector1`.  For example:

<h1 class="join"></h1>
```html
<!-- demo-child.html -->
<div class="blue">
	<h1>This text is not blue</h1>
	<p>This text is blue</p>
	<span>
		<p>This text is NOT blue,
			because its parent is the 
			span tag, which does not 
			have the "blue" class.
		</p>
	</span>
</div>
<p>This text is not blue</p>
```
```css
/* demo-child.css */
.blue > p {
	color: blue;
}
```
<h1 class="clear"></h1>

Finally, you can combine two selectors with a comma (`,`).  These two CSS files are the same:

<h1 class="join"></h1>
```css
/* demo.css */
p {
	color: blue;
}
.blue {
	color: blue;
}
```
```css
/* demo.css */
.blue, p {
	color: blue;
}
```
<h1 class="clear"></h1>

### 4.1.3 Basic Properties and Values

Learning CSS, for the most part, is about learning the knitty gritty details.  For an in-depth, comprehensive walkthrough of CSS properties and and how to apply them, check out [HTML Dog][htmldog]'s excellent [CSS tutorial series][htmldog-css]. In [section 4.2](#external-libraries), we will be applying CSS en-masse, using external libraries that provide shortcuts to a stylized webpage.  While using these libraries is good practice, these libraries always need to be accompanied by some extra CSS code for your own website.  For this reason, it's important to understand some basic CSS properties.

#### Color and Background-Color

You can change the background color of an element with the `background-color` attribute, just as you can change the text color with the `color` attribute.  There are many CSS properties that have colors as values, and for all of them colors can be represented in multiple ways ([detailed in-depth at MDN](mdn-colors)), the most simple (and limited) being *keywords* (like `blue`, `red`, etc.).

<h1 class="join"></h1>
```html
<!-- demo-color.html -->
<body>
	<p class="blue">
		This text is blue.
	</p>
	<p class="b-and-y">
		This text is yellow on black.
	</p>
</body>
```
```css
/* demo-color.css */
.blue { 
	color: blue;
}
.b-and-y {
	color: yellow;
	background-color: black;
}
```
<h1 class="clear"></h1>


#### Height and Width

The most basic CSS property is `height` and `width`.  They change the size of the *content area* of the selected element.  Height and weight take measurements of length ([detailed in depth at MDN][mdn-length]), the simplest being *pixels*, or *px*. 

<h1 class="join"></h1>
```html
<!-- demo-height-width.html -->
<body>
	<div class="blue first"></div>
	<div class="red second"></div>
	<div class="blue third"></div>
</body>
```
```css
/* demo-height-width.css */
.blue { background-color: blue; }
.red { background-color: red; }
.first {
	height: 100px;
	width: 200px;
}
.second {
	height: 150px;
	width: 150px;
}
.third {
	height: 50px;
	width: 300px;
}
```
<h1 class="clear"></h1>

![demo-height-width](img/demo-height-width.png)

#### Borders

You can also give your elements borders.  To create a visible border, you need to set three properties for the selected element: `border-width`, `border-style`, and `border-color`.  These three properties can be combined into one `border` attribute.  The values `width`, `style`, and `color` can be provided in any order.  The border will wrap around the box, not the text (note that the third resized `<p>` has a square border).

<h1 class="join"></h1>
```html
<!-- demo-height-width.html -->
<body>
	<p class="first">
		Black border, 3px wide.
	</p>
	<p class="second">
		Same as above
	</p>
	<p class="third">
		A thick, dashed blue border.
	</p>
</body>
```
```css
/* demo-border.css */
.first {
	border-width: 3px;
	border-style: solid;
	border-color: black;
}
.second {
	border: 3px solid black;
}
.third {
	height: 100px;
	width: 100px;
	border: 10px dashed blue;
}
```
<h1 class="clear"></h1>

![demo-border](img/demo-border.png)

#### Margin and Padding

Setting the `margin` and `padding` attributes for an element creates space around it.  The content area (changed by the `height` and `width` properties) border, margin, and padding make up the *box model*.  

![boxmodel](img/boxmodel.png)

*Photo credit to the [MDN page on the box model][mdn-box-model].*

For the most part, margin is used to create space outside of the element, and padding is used to make space inside the element.  The border sits just between the two.  

You can set margins with the `margin-top`, `margin-right`, `margin-bottom`, and `margin-left` attributes, and you can set padding with the `padding-top`, `padding-right`, `padding-bottom`, and `padding-left` attributes.  Values for these attributes are in units of length, and can even be negative.

The four margin and padding attributes can each be combined into `margin` and `padding`, and depending on how many arguments are provided, different of these properties will be set.  See the table for the details of how this works (`margin` is used, but the same goes for `padding`).

CSS | Shorthand | `-top` | `-right` | `-bottom` | `-left`
----|----|----|----|----|----
`margin: 1px 2px 3px 4px` | `T R B L` | `1px` | `2px` | `3px` | `4px`
`margin: 1px 2px 3px`     | `T R&L B` | `1px` | `2px` | `3px` | `2px`
`margin: 1px 2px`         | `T&B R&L` | `1px` | `2px` | `1px` | `2px`
`margin: 1px`             | `T&R&B&L` | `1px` | `1px` | `1px` | `1px`

Here are a couple different examples of padding and margins in action:

<h1 class="join"></h1>
```html
<!-- demo-height-width.html -->
<body>
	<div class="first">One</div>
	<div class="second">Two</div>
	<div class="third">Three</div>
</body>
```
```css
/* demo-margin-padding.css */
body {
	/* so that the effects of margins on the divs are easier to see. */
	margin: 0;
	padding: 0;
	border: 50px solid green;
}
div {
	/* Every div starts off as a yellow square with a black border. */
	height: 50px;
	width: 50px;
	background-color: yellow;
	border: 2px solid black;
}
.first {
	/* Offset from the wall on the left. */
	margin-left: 20px;
}
.second {
	/* Offset from block one by 50px. */
	margin-top: 50px;
	/* And the wall by 5px. */
	margin-left: 5px;
	/* 20px larger in each dimension because padding is inside the border, but text is offset by 20px (that's why the text doesn't hug the border). */
	padding:20px;
}
.third {
	/* Offset from the bottom by 10px, and 25px higher and to the left than expected because of the negative values. */
	margin: -25px 0 10px -25px;
	/* Taller with the text separated from the top of the box. */
	padding-top:20px;
}
```
<h1 class="clear"></h1>

![demo-margin-padding](img/demo-margin-padding.png)

<a id="using-the-inspector"></a>
### 4.1.4 Using the Inspector

One of the most important skills to learn as a web developer writing CSS is to learn how to use the inspector in your favorite browser (Internet Explorer not allowed).  The inspector lets you see the HTML, CSS, and JavaScript that your web browser is rendering, live!  You can inspect your own web page to find bugs or make tweaks to your code, or inspect other pages to learn how to imitate a desired HTML/CSS/JS effect.

With a web page open in FireFox, there are [three ways to inspect the page][inspect-ff]:

-   Choose the "Inspector" option from the "Web Developer" menu (which is a submenu in the "Tools" menu on the Mac).
-   Press `Ctrl`+`Shift`+`C` (`Cmd`+`Option`+`C` on the Mac OS X and Linux).
-   Right-click an element on a web page and select "Inspect Element".

With a web page open in Chrome, there are [three ways to inspect the page][inspect-chrome]:

-   Select the Chrome menu  at the top-right of your browser window, then select Tools > Developer tools.
-   Use `Ctrl`+`Shift`+`I` (or `Cmd`+`Opt`+`I` on Mac) to open the DevTools.
-   Right-click on any page element and select Inspect element.

To [inspect a page in Safari][inspect-safari], you first have to enable the Develop menu. Go into Safari's preferences, and check the “Show Develop menu in menu bar” checkbox in the "Advanced" pane. Then, you open the inspector in three ways:

-   Choose the "Show Web Inspector" option in the "Develop" menu.
-   Press `Cmd`+`Option`+`I`.
-   Right-click an element on a web page and select "Inspect Element".

<a href="#top" class="top" id="external-libraries">Top</a>
## 4.2 External Libraries

Building an entire web app from scratch can be an undertaking.  In order to speed up the process, many web developers use *front-end frameworks*, which are packages of HTML, CSS, and JavaScript that can be included in your web app.

The two most famous front-end frameworks are [Twitter Bootstrap][bootstrap] and [Foundation by Zurb][foundation].  Which one is better to use is up for debate, but if you believe [this Medium post][medium-bootstrap-vs-foundation], then the difference can be articulated fairly plainly:

> ZURB and Twitter made their objectives and intentions very clear when naming each CSS Frameworks: Bootstrap will have everything you’ll ever need to bootstrap your project. Foundation will have just the things you will ever need as the foundation for your project. 

We'll be using Foundation, because it's slimmer and simpler, and will provide a strong backbone for our app. You should keep [Foundation's newly revamped documentation][foundation-docs] open at all times for this section &mdash; it's a great reference tool.  

One other thing before we get started: on the Foundation website, you will continue to see references to "Sass" or "SCSS".  These are languages that extend the CSS syntax. They are more powerful, but harder to learn and develop in for the first time.  We are using "Foundation CSS", which is Foundation that uses raw CSS instead of Sass.  When we go onto the documentation page for different Foundation components you will see a section called "Customize with Sass" at the bottom.  For the purposes of our app, we can ignore this. 

<a id="installation-and-template-setup"></a>
### 4.2.1 Installation and Template Setup

Installing Foundation is as easy as 1 2 3.

#### 1. Download

Go to [the Foundation download page][foundation-download] and click the blue "Download Foundation CSS" button.  It will download the latest version of Foundation 5 (5.0.3 at the time of writing) in a zip file called `foundation-5.0.3.zip`.

#### 2. Integrate

Unzip `foundation-5.0.3.zip`.  Inside, you'll see a couple of files and folders, but the ones we care about are `css` and `js`.  Remember how we have a `css` and `js` folder under the `static` folder of our Flask app?  Copy all the files from `<Download_Directory>/foundation-5.0.3/css` into `<Project_Directory>/static/css` and all the files from `<Download_Directory>/foundation-5.0.3/js` into `<Project_Directory>/static/js`.

> Curious what Foundation looks like?  You could poke around the Foundation documentation, or open `index.html` with all the CSS and JS still in the `foundation-5.0.3` folder.  Pretty slick looking!

#### 3. Template

On the bottom of the "Getting Started With Foundation CSS" page, Zurb includes a section called [HTML Page Markup][foundation-html], which has a boilerplate for a basic Foundation app, reproduced here:

```html
<!DOCTYPE html> 
<!--[if IE 9]><html class="lt-ie10" lang="en" > <![endif]--> 
<html class="no-js" lang="en" > 
	
<head> 
  <meta charset="utf-8"> 
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
  <title>Foundation 5</title> 

  <!-- If you are using CSS version, only link these 2 files, you may add app.css to use for your overrides if you like. --> 
  <link rel="stylesheet" href="css/normalize.css"> 
  <link rel="stylesheet" href="css/foundation.css"> 

  <!-- If you are using the gem version, you need this only --> 
  <link rel="stylesheet" href="css/app.css"> 
  <script src="js/vendor/modernizr.js"></script> 
</head> 
<body> 
  
  <!-- body content here --> 

  <script src="js/vendor/jquery.js"></script> 
  <script src="js/foundation.min.js"></script> 
  <script> 
  	$(document).foundation(); 
  </script> 
</body> 
</html>
```

Because we are building an app in Flask however, we are going to take advantage of the Jinja2 templating that we discovered in [section 3.2](#templating-in-flask).  Foundation recommends that all the pages for our app have this boilerplate, so we'll make a Flask Template out of it that all of the rest of our pages will inherit.

Let's start with our base template.  Copy Foundation's boilerplate code (above) into a new file in the `templates` directory called `base.html`.  We'll make some modifications to make this template work with Flask.

First, let's focus on the `<head>` element.  Feel free to remove their comments, and let's change the title to be more modular, by making it a Jinja2 `{% block %}` that we can extend with other templates:

```html
...
<head> 
  <meta charset="utf-8"> 
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
  <title>{% block title %}{% endblock %}</title> 

  <link rel="stylesheet" href="css/normalize.css"> 
  <link rel="stylesheet" href="css/foundation.css"> 
  <link rel="stylesheet" href="css/app.css"> 

  <script src="js/vendor/modernizr.js"></script> 
</head>
...
```

Now whatever we put put in the `title` block in the child template will show up as the `<title>` of the page.  Note that we also link to `css/app.css`, which is for CSS code specific to our app (Never edit any of the foundation files!).  Create an empty file called `app.css` in the `css` folder, that we will add code to later:

```css
/* app.css */
```

We also should provide a `body` block, where the content of the child page will go:

```html
... 
<body> 

  {% block body %}{% endblock %}

  <script src="js/vendor/jquery.js"></script> 
...
```

Finally, we need to modify the imports.  Because the Flask directory structure is more complicated, the path from the HTML document to the `css` directory is more complicated.  To deal with this,  Flask provides a shortcut to the `static` directory that we can embed in our HTML document, so that even if we rearrange where the `static` directory is, our templates will always find the CSS files.

Everywhere we have `href` or `src` attributes `="<filename>"`, we'll replace it with `="{{ url_for('static', filename='<filename>') }}"`.   The `{{ }}` indicates a Jinja2 variable, and then the `url_for()` function provided by flask gets the URL of the file with path `'<filename>'` from the `'static'` folder.  Here is our completed `base.html`:

```html
<!DOCTYPE html>
<!--[if IE 9]><html class="lt-ie10" lang="en" > <![endif]-->
<html class="no-js" lang="en" >

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{% block title %}{% endblock %}</title>

  <link rel="stylesheet" href="{{ url_for('static', filename='css/normalize.css') }}">
  <link rel="stylesheet" href="{{ url_for('static', filename='css/foundation.css') }}">
  <link rel="stylesheet" href="{{ url_for('static', filename='css/app.css') }}">

  <script src="{{ url_for('static', filename='js/vendor/modernizr.js') }}"></script>
</head>
<body>
  {% block body %}{% endblock %}

  <script src="{{ url_for('static', filename='js/vendor/jquery.js') }}"></script>
  <script src="{{ url_for('static', filename='js/foundation.min.js') }}"></script>
  <script>
  	$(document).foundation();
  </script>
</body>
</html>
```

It's a bit messy, and definitely pretty long for a web page without any content, but that's why we'll relegate all our imports to this file.

All that's left to do is modify `hello.html`, `search.html` to extend from `base.html` (using both the `body` and `title` blocks).  Why not `results.html`? Because it already extends from `search.html` so we have our bases covered there. *This is exactly why we use template inheritance &mdash; so that our templates are simple, short, and to make refactoring easy.*

<h1 class="join"></h1>
```html
{% extends "base.html" %}
<!-- hello.html -->
{% block title %}
Hello World!
{% endblock %}

{% block body %}
<h1>Hello World!</h1>
<p>This is a <em><strong>really</strong> cool</em> paragraph.  My favorite search engine is <a href="http://www.google.com">Google</a></p>
{% endblock %}
```
```html
{% extends "base.html" %}
<!-- search.html -->
{% block title %}
Search | Has it Been Made Yet?
{% endblock %}

{% block body %}
<h1>Search</h1>
<form action="/search" method="post">
  <input type="text" 
    placeholder="Search for your idea" 
    name="user_search" required/>
  <button type="submit">Search</button>
</form>
{% block results %}{% endblock %}
{% endblock %}
```
<h1 class="clear"></h1>

It also might be nice to update our `hello.html` to reflect the purpose of our web app. (We've moved far beyond "Hello World".) The link to `"/search"` will send users to `yourapp.com/search`, or in our local development case `localhost:5000/search`.

```html
{% extends "base.html" %}
<!-- hello.html -->
{% block title %}Welcome | Has it Been Made Yet?{% endblock %}

{% block body %}
<h1>Has it Been Made Yet?</h1>
<h2>A tool for hackers with "unique" ideas.</h2>
<a href="/search">Launch</a>
{% endblock %}
```

<a id="using-foundation"></a>
### 4.2.2 Using Foundation

Using Foundation can be as simple as applying some extra classes to HTML elements, applying the imported CSS.  For general purpose "style-based" changes this is fine. (The class `button` will make an `<a>` tag look like a button, and so on. Just look up the component your are styling in the [Foundation docs][foundation-docs] and you'll be fine.) While Foundation offers many shortcuts to attractively styled pages, it also provide "layout-based" classes that are used for placing elements appropriately on the page.  Chief among these is Foundation's [grid system][foundation-grid].

The grid system makes layout easy.  A `<div>` with class `row` hold 12 columns, and then you can create `<div>`s that take up any number of those columns.  For example, the following would create three side-by-side columns:

```html
<div class="row">
  <div class="large-4 columns">Left</div>
  <div class="large-4 columns">Middle</div>
  <div class="large-4 columns">Right</div>
</div>
```

Foundation's grid system is *responsive*, meaning that it adapts to different screen sizes.  `small` is every screen from 0-640px, `medium` is 641-1024px, and `large` is 1025px and up.  The numbers after the `large-`, `medium-`, `small-` classes to be how many columns that `<div>` takes up at that range and up.  These numbers jump to 12 when you go below the size before the `-`.  So for our example, as soon as the screen is resized to less than 1025px all three of the `columns` become 12 columns wide (taking up the entire row, and thusly being stacked on top of each other.)  If we refactored like this:

```html
<div class="row">
  <div class="small-4 columns">Left</div>
  <div class="small-4 columns">Middle</div>
  <div class="small-4 columns">Right</div>
</div>
```

they would remain 4 columns no matter how small the screen was.  

What about this code?: 

```html
<div class="row">
  <div class="small-6 medium-4 large-3 columns">Left</div>
  <div class="small-6 medium-4 large-6 columns">Middle</div>
  <div class="medium-4 large-3 columns">Right</div>
</div>
```

Well, at screens wider than 1024px, we have 3,6,3, so the middle `<div>` will be twice as large as the ones on the sides.  Then, between 641-1024px, all three are the same size.  Finally, on screens 640px and narrower, the left and the right `<div>`s are half the screen, and the right columns overflows to be on it's next line. (The `small-#` class is not defined on the third `<div>`, so it becomes 12 columns wide.)

The grid system can be a little daunting, but with practice and [the documentation][foundation-grid] at hand, it is manageable.

<a id="rewriting-templates"></a>
### 4.2.3 Rewriting Templates

Let's rework our app to look good &mdash; with Foundation!

#### hello.html

We want this to be the landing page for our search app.  It could be a big, full page image with a box in the middle of the screen that has the name and tagline for our app. 

First, let's make the box.  Start by wrapping the content of the page in a `row` and `columns` `<div>`.  `medium-9` should suffice, we want it to be fairly large, but not the whole width of the screen.

```html
{% extends "base.html" %}
<!-- hello.html -->
{% block title %}Welcome | Has it Been Made Yet?{% endblock %}

{% block body %}
<div class="row">
  <div class="medium-9 columns">
    <h1>Has it Been Made Yet?</h1>
    <h2>A tool for hackers with "unique" ideas.</h2>
    <a href="/search">Launch</a>
  </div>
</div>
{% endblock %}
```

We could center the `columns` `<div>` ourselves, but Foundation coveniently let's us center any `columns` element with the `small-centered`, `medium-centered`, and `large-centered` classes.  Apply `medium-centered` to center our `<div>`.

```html
<div class="medium-9 medium-centered columns">
```

We can easily turn our "Launch" `<a>` tag into a button with just the `button` class. That was easy!

```html
<a class="button" href="/search">Launch</a>
```

Next, we'll make the background an image.  We can do this in pure CSS, no `<img>` tag necessary!  To make a background image, you must first make sure that the `<html>` and `<body>` tags are taking up the entire browser window.  Just as we can measure length in px, we can also measure in percent (`%`).  This is perfect for our purposes.  Edit `app.css`:

```css
body, html {
	height: 100%;
	width: 100%;
}
```

To set the actual image, we'll be using the `background` property on the `body` element.  For a detailed description of it's usage, check out the [MDN page][mdn-background].  We'll be setting  `background-color` (for fallback), `background-image`, `background-repeat`, `background-attachment`, and `background-position`.

```css
body {
	background-color: black;
	/* feel free to use any image you want.  The url() function will take local or internet images */
	background-image: url(http://i0.wp.com/devleader.ca/wp-content/uploads/2014/01/php_code.jpg);
	background-repeat: no-repeat;
	background-attachment: fixed;
	background-position: center center;
}
```

or more succinctly:

```css
body {
	background: black url(http://i0.wp.com/devleader.ca/wp-content/uploads/2014/01/php_code.jpg) no-repeat fixed center center;
}
```

Refresh the page. It looks good, but not great; the text is too hard to read.  Let's put our text in a box, so it's easier to see off the background.  Conveniently, Foundation has a `panel` class that will work well for us.  Wrap the text in a `<div>` with the `panel` class and see how it looks.

```html
{% block body %}
<div class="row">
  <div class="medium-9 medium-centered columns">
    <div class="panel">
      <h1>Has it Been Made Yet?</h1>
      <h2>A tool for hackers with "unique" ideas.</h2>
      <a class="button" href="/search">Launch</a>
    </div>
  </div>
</div>
{% endblock %}
```

The panel looks good, but it's stuck to the top of the page, which doesn't look great.  Let's bring it down some by adding `margin` to the `row`.  We don't want *all* rows to have margin at the top (what if we make another `row` later?), so we should add a class.  `10%` margin should do.

<h1 class="join"></h1>
```html
{% block body %}
<div class="row splash-page">
  <div class="medium-9 medium-centered columns">
	<div class="panel">
...
```
```css
...
.splash-page {
	margin-top: 10%;
}
```
<h1 class="clear"></h1>

The panel would look much better if the text were center-aligned.  Use the descendant selector to select the panel, and then set it's `text-align` property to `center`.

```css
.splash-page .panel {
	text-align: center;
}
```

This is looking great!  The only other thing that might be nice is to add a little transparency to our panel.  Using the `rgba()` CSS function (Red, Green, Blue, Alpha), we can set this.  Use [your inspector](#using-the-inspector) to figure out the RGB values on the background color of the `panel` `<div>`.  It should be `#f2f2f2`, or `rgb(242,242,242)`.  Let's set the alpha, or transparency to 0.9 (on a scale from 0.0 to 1.0 where 0.0 is clear and 1.0 is solid).

```css
.splash-page .panel {
	text-align: center;
	background-color: rgba(242, 242, 242, 0.9);
}
```

And there we have it, a finished `hello.html`!

![madeyet-1](img/madeyet-1.png)

#### search.html

Our second refactor should go faster. Start by wrapping the form in a row, column, and panel same as before.  We don't want the actual app to take up three quarters of the page, so we can use `large-12 columns` instead of `medium-9 medium-centered columns`.

```html
{% extends "base.html" %}
<!-- search.html -->
{% block title %}Search | Has it Been Made Yet?{% endblock %}

{% block body %}
<div class="row">
  <div class="large-12 columns">
    <div class="panel">
      <h1>Search</h1>
      <form action="/search" method="post">
        <input type="text" placeholder="Search for your idea" name="user_search" required/>
        <button type="submit">Search</button>
      </form>
      {% block results %}{% endblock %}
    </div>
  </div>
</div>
{% endblock %}
```

Let's put the search button on the same line as the search box, at a 10:2 ratio.  We can use the `collapse` class on the `row` so that the search box touches the search button.

```html
...
<form action="/search" method="post">
  <div class="row">
  	<div class="small-10 columns">
	  <input type="text" placeholder="Search for your idea" name="user_search" required/>
    </div>
    <div class="small-2 columns">
	  <button type="submit">Search</button>
    </div>
  </div>
</form>
...
```

This already looks all right, but it might be nice to attach the search button to the search box.  Exploring the ["forms" page on Foundations documentation][foundation-forms], we see that if we just apply the `postfix` class to our button, it will change to be the same height as the the search box:

```html
<button class="postfix" type="submit">Search</button>
```

There's really only one more thing that would make this page look better, and it's to keep the search panel from sticking completely to the top.  Let's put 20 pixels of padding on the `<body>`, so that it looks uniform with the bottom.

```css
body {
	padding-top: 20px;
	background: black url(http://i0.wp.com/devleader.ca/wp-content/uploads/2014/01/php_code.jpg) no-repeat fixed center center;
}
```

Nice!

![madeyet-2](img/madeyet-2.png)

#### results.html

Once again, our smart templating has done us a service; the results page looks pretty good!  We can make just a few adjustments to finish it off.

Let's get rid of the dots on our unordered list.  Foundation [has a class for this][foundation-lists], just give our `<ul>` the `no-bullet` class and we're good to go.

```html
...
<ul class="no-bullet">
	{% for repo in api_data["items"] %}
...
```

We can also make the "by <username>" part of the header smaller with the `<small>` tag (that's a [Foundation feature][foundation-small], so don't use it in other projects. In fact, the `<small>` tag is discouraged in HTML5).

```html
<h3>{{ repo.name }} <small>by {{ repo.owner.login }}</small></h3>
```

And we're done!

![madeyet-3](img/madeyet-3.png)

Congratulations!  You've built a complete web application in Flask!  The Flask server loads the templates for our different routes, and then makes calls to the Github search API and returns the data to the client.  Pretty impressive!

Push yourself to try some of the extensions throughout this document, they offer some interesting challenges. 

<!-- python/flask -->
[flask]: http://flask.pocoo.org/
[route]: http://flask.pocoo.org/docs/quickstart/#routing
[decorators]: https://wiki.python.org/moin/PythonDecorators
[py-requests]: http://docs.python-requests.org/en/latest/
[py-requests-basic-auth]: http://docs.python-requests.org/en/latest/user/authentication/#basic-authentication
[pip]: http://www.pip-installer.org/en/latest/
[py-response-obj]: http://docs.python-requests.org/en/latest/api/#requests.Response
[flask-jsonify]: http://flask.pocoo.org/docs/api/#flask.json.jsonify
[multidict]: http://werkzeug.pocoo.org/docs/datastructures/#werkzeug.datastructures.MultiDict
[render-template]: http://flask.pocoo.org/docs/quickstart/#rendering-templates
[jinja2]: http://jinja.pocoo.org/docs/templates/
[jinja2-for]: http://jinja.pocoo.org/docs/templates/#for
[jinja2-block]: http://jinja.pocoo.org/docs/templates/#template-inheritance

<!-- github -->
[github]: http://github.com
[github-search-docs]: http://developer.github.com/v3/search/
[github-search-docs-repos]: http://developer.github.com/v3/search/#search-repositories
[github-rate-limiting]: http://developer.github.com/v3/#rate-limiting
[github-search-rate-limiting]: http://developer.github.com/v3/search/#rate-limit
[github-basic-auth]: http://developer.github.com/v3/auth/#other-authentication-methods
[github-new-token]: http://developer.github.com/v3/oauth/#create-a-new-authorization
[github-token-scopes]: http://developer.github.com/v3/oauth/#scopes
[github-token-auth]: http://developer.github.com/v3/#oauth2-token-sent-as-a-parameter
[github-api-docs-pagination]: http://developer.github.com/v3/#pagination

<!-- networking -->
[port]: http://en.wikipedia.org/wiki/Port_(computer_networking)
[localhost]: http://en.wikipedia.org/wiki/Localhost
[client-server]: http://en.wikipedia.org/wiki/Client%E2%80%93server_model
[dynamic-content]: http://en.wikipedia.org/wiki/Dynamic_content
[api]: http://en.wikipedia.org/wiki/Api
[rest-api]: http://en.wikipedia.org/wiki/REST_API
[open-source]: http://en.wikipedia.org/wiki/Open_source
[json]: http://en.wikipedia.org/wiki/Json
[https]: http://en.wikipedia.org/wiki/Https
[urls]: http://en.wikipedia.org/wiki/Uniform_resource_locator
[url-google]: http://www.mattcutts.com/blog/seo-glossary-url-definitions/
[url-wikipedia]: http://en.wikipedia.org/wiki/URI_scheme#Generic_syntax
[basic-http-auth]: http://en.wikipedia.org/wiki/Basic_access_authentication

<!--HTML-->
[html]: http://en.wikipedia.org/wiki/HTML/
[attributes]: http://en.wikipedia.org/wiki/HTML_attribute
[href-confusion]: http://tomayko.com/writings/wtf-is-an-href-anyway
[doctype]: http://en.wikipedia.org/wiki/Doctype#HTML5_DTD-less_DOCTYPE
[mdn]: https://developer.mozilla.org/en-US/
[mdn-elements]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element
[mdn-body]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/body
[mdn-div]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div
[mdn-head]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head
[mdn-link]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link
[mdn-html]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html
[mdn-span]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/span
[mdn-p]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p
[mdn-a]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a
[mdn-h1-6]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h1
[mdn-em]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/em
[mdn-strong]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/strong
[mdn-br]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br
[mdn-ol]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol
[mdn-ul]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul
[mdn-li]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li
[mdn-meta]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta
[mdn-DOCTYPE]: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5/Introduction_to_HTML5#Declaring_that_the_document_contains_HTML5_mark-up_with_the_HTML5_doctype
[mdn-style]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style
[mdn-title]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title
[mdn-img]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img
[mdn-script]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script
[mdn-form]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form
[mdn-form-usage]: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms/My_first_HTML_form?redirectlocale=en-US&redirectslug=HTML%2FForms%2FMy_first_HTML_form
[mdn-input]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input
[mdn-label]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label
[mdn-textarea]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea
[mdn-button]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button

<!-- CSS -->
[css]: http://en.wikipedia.org/wiki/Css
[htmldog]: http://htmldog.com
[htmldog-css]: http://htmldog.com/guides/css/
[mdn-colors]: https://developer.mozilla.org/en-US/docs/Web/CSS/color_value
[mdn-length]: https://developer.mozilla.org/en-US/docs/Web/CSS/length
[mdn-box-model]: https://developer.mozilla.org/en-US/docs/Web/CSS/box_model
[medium-bootstrap-vs-foundation]: https://medium.com/frontend-and-beyond/8b3812c7007c
[bootstrap]: http://getbootstrap.com/getting-started/
[foundation]: http://foundation.zurb.com
[foundation-docs]: http://foundation.zurb.com/docs/css.html
[foundation-html]: http://foundation.zurb.com/docs/css.html#html-page-markup
[foundation-grid]: http://foundation.zurb.com/docs/components/grid.html
[mdn-background]: https://developer.mozilla.org/en-US/docs/Web/CSS/background
[foundation-forms]: http://foundation.zurb.com/docs/components/forms.html
[foundation-lists]: http://foundation.zurb.com/docs/components/typography.html#lists
[foundation-small]: http://foundation.zurb.com/docs/components/typography.html#small-header-segments

<!-- tools -->
[curl-win]: http://curl.haxx.se/download.html
[curl]: http://curl.haxx.se/docs/manpage.html
[json-chrome]: https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc?hl=en
[json-firefox]: https://addons.mozilla.org/en-us/firefox/addon/jsonview/
[json-safari]: https://github.com/rfletcher/safari-json-formatter
[inspect-ff]: https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector
[inspect-chrome]: https://developers.google.com/chrome-developer-tools/
[inspect-safari]: https://developer.apple.com/library/mac/documentation/AppleApplications/Conceptual/Safari_Developer_Guide/GettingStarted/GettingStarted.html

<!-- Other resources -->
[learn]: http://adicu.com/learn
