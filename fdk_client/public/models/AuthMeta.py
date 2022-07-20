"""Public Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class AuthMeta(BaseSchema):
    # Webhook swagger.json

    
    type = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    

