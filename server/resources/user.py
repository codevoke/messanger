"""User endpoint"""
from flask_restx import Namespace, Resource, fields

from models import UserModel


api = Namespace("User", description="User methods to retrieve")

user = api.model(
    "User",
    {
        "id": fields.Integer(required=True, description="user ID"),
        "username": fields.String(required=True, description="user name"),
        "age": fields.Integer(required=True, description="user age")
    }    
)


@api.route('/user/<int:_id>')
@api.param("id", "the user identifier")
@api.param(404, "user not found")
class User(Resource):
    """open methods for retrieve users"""
    @api.doc("get user data")
    @api.marshal_with(user)
    def get(self, _id: int) -> UserModel | None:
        """return json view of user object or return abort(404)"""
        return UserModel.get(_id).json()
