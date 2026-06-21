from rest_framework.views import exception_handler


class BusinessError(Exception):
    def __init__(self, message, code="BUSINESS_ERROR", details=None):
        self.message = message
        self.code = code
        self.details = details or {}
        super().__init__(message)


def custom_exception_handler(exc, context):
    if isinstance(exc, BusinessError):
        from rest_framework.response import Response

        return Response({"code": exc.code, "message": exc.message, "details": exc.details}, status=400)
    response = exception_handler(exc, context)
    if response is not None:
        return response
    from rest_framework.response import Response

    return Response({"code": "INTERNAL_ERROR", "message": str(exc), "details": {}}, status=500)

