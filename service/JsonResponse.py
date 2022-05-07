from flask import g


class JsonResponse:
    def __init__(self, status="", error="", reason="", data=[], code= 0):
        self.__reason = reason
        self.__status = status
        self.__data = data
        self.__code = code

    def get_code(self):
        return self.__code

    def set_code(self, code):
        self.__code = code

    def get_reason(self):
        return self.__reason

    def set_reason(self, reason):
        self.__reason = reason

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def returnResponse(self):
        response = {
            "status": self.__status,
            "reason": self.__reason,
            "code": self.__code,
            "data": self.__data,
        }
        g.response = response
        return response
