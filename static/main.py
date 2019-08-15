from browser import document as doc
from browser import bind, ajax, html

import urllib.request
import urllib.parse
import os

print("Hello from the backend")

BASE_URL = "{}/api/todo".format(os.getcwd())
print("CURRENT WORKING DIR: ", BASE_URL)



@bind('#form_submit', 'click')
def add_to_do(ev):
    url = os.path.join(BASE_URL, 'create/')
    text = doc["form_text_input"].value
    req = ajax.ajax()
    req.bind('complete', on_complete)
    # send a POST request to the url
    req.open('POST', url, True)
    req.set_header('content-type','application/x-www-form-urlencoded')
    # send data as a dictionary
    req.send({'text': text })

def on_complete(req):
    if req.status==200 or req.status==0:
        print(req)
        print(req.text)
    else:
        print("ERROR: " + req.text)


"""
Uses a decorator to bind #GET_button's click event to the function
AFAIK only the standard library is available. So no requests :(

This is only an example, and isn't part of the todo app
"""
@bind("#GET_button", "click")
def get(ev):
    url = BASE_URL
    response = urllib.request.urlopen(url)
    print(response.read())
