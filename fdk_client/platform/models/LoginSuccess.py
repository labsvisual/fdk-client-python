"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .UserSchema import UserSchema






class LoginSuccess(BaseSchema):
    # User swagger.json

    
    user = fields.Nested(UserSchema, required=False)
    
    request_id = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    

