from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

# Middleware para manejo de excepciones
class ExceptionHandlingMiddleware:
    def __init__(self, app):
        self.app = app
        self.app.before_request(self.before_request)
        self.app.after_request(self.after_request)
        self.app.register_error_handler(Exception, self.handle_exception)

    def before_request(self):
        pass  # Aquí puedes agregar lógica para ser ejecutada antes de cada solicitud

    def after_request(self, response):
        return response

    def handle_exception(self, e):
        if isinstance(e, HTTPException):
            response = jsonify({
                "message": e.description
            })
            response.status_code = e.code
        else:
            response = jsonify({
                "message": "An unexpected error occurred",
                "detail": str(e)
            })
            response.status_code = 500
        return response
