from cached_property import cached_property
from flask import request, make_response
from flask.views import MethodView
from ..utils import json_loads, json_dumps_unicode


class LittleRedBBC(MethodView):

    @cached_property
    def result(self) -> str:
        return json_dumps_unicode({
            "data": {
                "package_id": "id_value"
            },
            "error_msg": None,
            "error_code": 0,
            "success": True
        })

    def get(self):
        return self.result

    def post(self):
        data = json_loads(request.data)
        type(data)

        response = make_response(self.result.replace("id_value", "test"))
        response.headers = {
            "content-type": "application/json;charset=utf8"
        }
        return response
