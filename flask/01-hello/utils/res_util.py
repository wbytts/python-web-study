from flask import jsonify


class Result(object):
    def __init__(self, msg="success", data=None, result=True, code=200) -> None:
        super().__init__()

        self.result = result
        self.code = code
        self.data = data
        self.msg = msg

    def json(self):
        return jsonify({
            "result": self.result,
            "msg": self.msg,
            "code": self.code,
            "data": self.data
        })
