"""User endpoint"""
from flask_restx import Namespace, Resource, fields, reqparse
from flask import abort
from models import UserModel
from __jwt__ import generate_token


api = Namespace("Auth", description="Authorization in messanger")

user = api.model(
    "User",
    {
        "id": fields.Integer(required=True, description="user ID"),
        "username": fields.String(required=True, description="user name"),
        "age": fields.Integer(required=True, description="user age"),
        "access_token": fields.String(required=True, description="access token for private methods")
    }    
)


login_parser = reqparse.RequestParser()
login_parser.add_argument("login", type=str, required=True, help="`login` is required field")
login_parser.add_argument("password", type=str, required=True, help="`password` is required field")


@api.route('/login')
@api.param(400, "login or password are incorrect")
class Login(Resource):
    """Login method"""
    @api.doc("Authorize and get access_token")
    @api.marshal_with(user)
    @api.expect(login_parser)
    def post(self):
        """login user in messaner andreturn access code or 400"""
        args = login_parser.parse_args()
        User = UserModel.auth(args["login"], args["password"])

        if User is None:
            abort(400, message="Invalid credentials!")

        
