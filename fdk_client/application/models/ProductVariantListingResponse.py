"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductVariantItemResponse import ProductVariantItemResponse










class ProductVariantListingResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductVariantItemResponse, required=False), required=False)
    
    total = fields.Int(required=False)
    
    key = fields.Str(required=False)
    
    display_type = fields.Str(required=False)
    
    header = fields.Str(required=False)
    

