"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class CreateUserSessionResponseSchema(BaseSchema):
    # User swagger.json

    
    domain = fields.Str(required=False)
    
    max_age = fields.Float(required=False)
    
    secure = fields.Boolean(required=False)
    
    http_only = fields.Boolean(required=False)
    
    cookie = fields.Dict(required=False)
    

