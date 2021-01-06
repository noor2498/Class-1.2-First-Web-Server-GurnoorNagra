# Your First Web Server
&nbsp;
### Goals:
1. Install and setup a basic web application using Flask
&nbsp;
## Installing Python packages

Installing Python packages in Repl.it is very easy.

&nbsp;
>1. From the left-hand menu bar, select the `Packages` icon. You will be able to see all the packages you have currently installed.

![Packages](https://mcusercontent.com/040e2f3f9d74f0f1ed3abc80a/images/0d3e772f-0f45-4ff8-ab73-f3631ea4e892.png)
&nbsp;
>2. Simply search for package you want to install. Here, we search for a package called `Flask` and then press the `+` icon to install it. 

![Packages Install](https://mcusercontent.com/040e2f3f9d74f0f1ed3abc80a/images/02be99e7-090f-4e7d-b91b-c3b036446ce3.png)

You can see the detailed list of all your installed package in a file called `pyproject.toml`. If you then want to share your project while still in development, **you could share this file** and the recipient simply has to install the dependencies listed there. 

&nbsp;
## Python Terminology
Often, different terms are used to mean the same or similar thing so we are going to try and standardize terms to minimize confusion.

![Python terminology](https://www.miltonmarketing.com/wp-content/uploads/2018/04/python-programming-iv-program-components-functions-classes-modules-packages-11-638.jpg)

&nbsp;
1. **Package** - collection of Python code files, or **modules** which are generally used for a specific application. For example, in the next section, we will install the `Flask` package which is used to setup the infrastructure for web applications.

&nbsp;
2. **Module** - A file containing Python Classes and/or Functions. The file name is the module name with the suffix `.py` appended to it. So for example, a file called `covid19data.py` would represent a module called `covid19data`. **Modules** are designed for a specific assignment made up of a bunch of tasks and can contain multiple **Classes** and **Functions**

&nbsp;
3. **Class** - Serves as a **blueprint** or template or receipe for building Python components. **Everything in Python is an instance of some Class**. 

&nbsp;
4. **Function** - Fundamental code block which make up **Classes** and **Modules** and are generally designed for a single task. 

So in this course, we are building multiple **modules** consisting of **functions** and other statements, using existing community-built **packages**. 

**Clear as mud?**

&nbsp;
## What is a Web App?
A web application (or web app) is software which uses web browsers and runs on a web server to perform tasks over the internet. This is UNLIKE computer-based applications which are installed and run locally on your computer. 

At a high level, here is a diagram outlining the components of a web application:

![Web App](https://mcusercontent.com/040e2f3f9d74f0f1ed3abc80a/images/d461cc2e-b6f1-4d56-893d-9949a164b354.png)

A web server stores, processes and delivers web pages to clients (like your Chrome web browser). It:
* Takes incoming requests over the internet
* Identifies what information or data needs to be provided
* Provides a response to the incoming requests

Think of a web server **like an airport's air traffic controller** that:
* Directs inbound and outbound airplane traffic
* Directs local plane storage (at the gate)
* Provides local airport information and other key information to pilots

![Overall request response flow](https://mcusercontent.com/040e2f3f9d74f0f1ed3abc80a/images/291ac8cb-475d-45dc-838b-59dfe6c9aa79.png)

So when you go to a website like `https://www.python.org/` the following happens:

* Your browser makes a request call to the URL: `https://www.python.org/` which is made up of:
  * A Base URL: `python.org`
  * A route or endpoint: `/`

By default, the `/` endpoint is called the **index** route.

* Your browser is sending a request to the Python web server at the index (`/`) route.
* The web server then says: _'Ok, what data do I send when someone goes to the index route?'_ and finds that data.
* The web server then sends back all the data to the entity making the request (i.e. your browser)

Now if you click on the `Jobs` menu item on the webpage, you are doing the following:

* Your browser makes a request call to the URL: `https://www.python.org/jobs` which is made up of:
  * A Base URL: `python.org`
  * A route or endpoint: `/jobs`

* Your browser is sending a request to the Python web server at the `/jobs` route.
* The web server then says: _'Ok, what web page do I send when someone goes to the `/jobs` route?'_ and finds that data.
* The web server then sends back all the data to the entity making the request (i.e. your browser)

Let us see this in action!

&nbsp;
## Using Flask

Flask is a lightweight web framework that allows you to use Python to get a web app running. A key component to any framework supporting web applications is running a web server for you. Flask allows us to do this very quickly.

Recall that we already installed Flask earlier. To learn how to use this package, we refer to its **documentation**. 
&nbsp;
>1. Have a look at the quickstart example in the Flask Documentation: https://flask.palletsprojects.com/en/1.1.x/quickstart/

>2. Now in your `main.py`,copy and paste in the following template code. **Note the indentation!! This is VERY IMPORTANT in Python as we will see later!**

```
from flask import Flask
server = Flask(__name__)

@server.route('/')
def hello_world():
    return 'Hello, World!'
```

Let us breakdown what is going on here:

    from flask import Flask
    app = Flask(__name__)


* `flask` represents the package that we installed. The name of a specifc blueprint, or Class, we want to use is called `Flask`
&nbsp;
* We create an instance of this Class called `server`. Anything between `(...)` is called an *instruction* or *argument*. We will get to what the `__name__` argument means a bit later.


    @app.route('/')

Every web server defines one or many routes. Here, `'/'` refers to the index route of the web server. If our application had an `About Us` webpage, we might want to define a route like `'/about'` so that we can serve up the `About Us` webpage data when a client makes a request to `'/about'`. 

    def hello_world():
        return 'Hello, World!'

`hello_world()` is a function that gets run or called when a request is made to `'/'`. When that function gets called, it simply returns the string: `'Hello, World!'`. 

&nbsp;
>3. Finally, add the following code at the bottom of your `app.py` file:

    server.run(host='0.0.0.0', debug=True)

 All you currently need to know is that we can now run our Flask web server directly by simply clicking the `Run` button like before.

And there you go! **You have successfully setup a web server using Flask to run a basic web page!**

The information you see in your console window is called your **web server logs**. This provides us with some details about what the web server is doing. For example:

* We see that the app is running on `http://0.0.0.0:5000`. This is actually just a pass-through URL to the URL provided by Repl.it. 

* We are warned that Flask is a _"development server. Do not use it in a production deployment."_

* There is a **debugger** active. This is simply a built-in Flask tool to help us troubleshoot any issues.

&nbsp;
## Exercise

>1. Define an appropriate server routing which serves up the following function:

    def about_us():
        return 'This will be the About Us webpage'

    def covid19data():
        return 'This will contain covid19 related data'

>2. Save your file and then commit your work to Git and GitHub. 

&nbsp;
## Your Course Project
Now let us focus in on our course project and do the following:

> Create a new Python repl using the name of your own app that you want to build and go through the following steps again:
&nbsp;
1. Initiate local Git
&nbsp;
2. Setup your GitHub repository
&nbsp;
3. Install the `Flask` Python package
&nbsp;
4. Create a Flask server with the two following routes:
    - Index: `'/'` which returns the string `'Welcome to my homepage'`
    &nbsp;
    - About page: `'/about'` which returns the string `'Welcome to my about me page'`
&nbsp;
5. Save and commit your changes to your local Git
&nbsp;
6. Push your changes to your new GitHub repo
