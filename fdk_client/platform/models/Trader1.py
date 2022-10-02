"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class Trader1(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    address = fields.List(fields.Str(required=False), required=False)
    

