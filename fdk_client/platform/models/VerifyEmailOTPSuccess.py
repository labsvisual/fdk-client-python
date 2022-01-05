"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .UserSchema import UserSchema




class VerifyEmailOTPSuccess(BaseSchema):
    # User swagger.json

    
    user = fields.Nested(UserSchema, required=False)
    
    verify_email_link = fields.Boolean(required=False)
    

