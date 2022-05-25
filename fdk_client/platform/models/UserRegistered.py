"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class UserRegistered(BaseSchema):
    # Cart swagger.json

    
    end = fields.Str(required=False)
    
    start = fields.Str(required=False)
    

