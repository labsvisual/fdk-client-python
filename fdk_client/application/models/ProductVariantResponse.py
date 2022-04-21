"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ProductVariantItemResponse import ProductVariantItemResponse




class ProductVariantResponse(BaseSchema):
    # Catalog swagger.json

    
    header = fields.Str(required=False)
    
    display_type = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ProductVariantItemResponse, required=False), required=False)
    
    key = fields.Str(required=False)
    

