"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .UserSchema import UserSchema






class VerifyOtpSuccess(BaseSchema):
    # User swagger.json

    
    user = fields.Nested(UserSchema, required=False)
    
    user_exists = fields.Boolean(required=False)
    
    register_token = fields.Str(required=False)
    

