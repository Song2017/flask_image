from flask import render_template
from app.web.blue_print import web

# run code in different file
from app.web import index
from app.web.littlered_bbc import LittleRedBBC


@web.app_errorhandler(404)
def not_found(e):
    # AOP 思想
    return render_template('404.html'), 404


web.add_url_rule("/oms/xhs/packages",
                 view_func=LittleRedBBC.as_view("little_red_bbc"))
