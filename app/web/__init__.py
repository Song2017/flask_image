from flask import render_template
from app.web.blue_print import web

# run code in different file
from app.web import littlered_bbc
from app.web import index


@web.app_errorhandler(404)
def not_found(e):
    # AOP 思想
    return render_template('404.html'), 404
