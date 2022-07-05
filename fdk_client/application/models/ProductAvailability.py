"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class ProductAvailability(BaseSchema):
    # Cart swagger.json

    
    deliverable = fields.Boolean(required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
    other_store_quantity = fields.Int(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    is_valid = fields.Boolean(required=False)
    

