"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Trader(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    address = fields.Str(required=False)
    

