from . import web
from flask import request

print('red', id(web))


@web.route('/oms/xhs/packages', methods=['GET', "POST"])
def get_orders_from_red():
    print(request.form, request.args, request.data)
    return "asdf"
