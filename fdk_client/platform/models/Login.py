"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Login(BaseSchema):
    # User swagger.json

    
    password = fields.Boolean(required=False)
    
    otp = fields.Boolean(required=False)
    

