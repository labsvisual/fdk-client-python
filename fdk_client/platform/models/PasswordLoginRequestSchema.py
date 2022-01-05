"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class PasswordLoginRequestSchema(BaseSchema):
    # User swagger.json

    
    captcha_code = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
    username = fields.Str(required=False)
    

