"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SharedCart import SharedCart




class SharedCartResponse(BaseSchema):
    # Cart swagger.json

    
    cart = fields.Nested(SharedCart, required=False)
    
    error = fields.Str(required=False)
    

