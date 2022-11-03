"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class ProductSize(BaseSchema):
    # Catalog swagger.json

    
    quantity = fields.Int(required=False)
    
    is_available = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    
    seller_identifiers = fields.List(fields.Str(required=False), required=False)
    
    display = fields.Str(required=False)
    

