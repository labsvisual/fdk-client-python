"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class SendResetPasswordEmailRequestSchema(BaseSchema):
    # User swagger.json

    
    email = fields.Str(required=False)
    
    captcha_code = fields.Str(required=False)
    

