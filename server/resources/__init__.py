"""creating api from all namespace to use it in app.py"""
from flask_restx import Api

from .user import User


api = Api(
    title="Small messanger API",
    version="1.0",
    description="simple api for simple messanger"
)

api.add_namespace(User)
