from flask import make_response
import socket
import os

from . import web


@web.route('/', methods=['GET'])
def hello():
    html = "page"
    resp = make_response(html, 303)
    resp.headers = {
        "content-type": "text/plain",
        "location": 'http://www.baidu.com'
    }

    return resp


@web.route('/index/', methods=['GET'])
def hello_index():
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname} <br/>"
    html = html.format(name=os.getenv("NAME", "world"),
                       hostname=socket.gethostname())
    resp = make_response(html, 200)
    resp.headers = {
        "content-type": "text/html",
    }
    return resp
