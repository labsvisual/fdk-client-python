"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PriceRange(BaseSchema):
    # Cart swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    

