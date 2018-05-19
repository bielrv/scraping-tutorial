from urllib.request import urlopen
"""
Requests allows to send HTTP/1.1 requests using Python.
With it, you can add content like headers, form data, multipart files, and parameters
via simple Python libraries.
It also allows you to access the response data of Python in the same way.
The urllib module in Python 3 allows you access websites via your program.
This opens up as many doors for your programs as the internet opens up for you.
"""

from bs4 import BeautifulSoup
"""
Python library for pulling data out of HTML and XML files.
It works with your favorite parser to provide idiomatic ways of navigating, searching, ...
"""

# Handling HTTP Exceptions
try:
    html = urlopen("https://www.python.org/")
    # urlopen is used to connect to the websites
    type(html)
    print(html)
    # html points to the HTTPResponse
except HTTPError as e:
    print(e)
else:
    res = BeautifulSoup(html.read(),"html5lib");
    # html.read() is used to read the html

    type(res)
    # res is a BeautifulSoup object containing html response which has a hieratical structure

    print(res.title)
