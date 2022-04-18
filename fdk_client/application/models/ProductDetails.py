"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










































class ProductDetails(BaseSchema):
    # Catalog swagger.json

    
    has_variant = fields.Boolean(required=False)
    
    attributes = fields.Dict(required=False)
    
    item_code = fields.Str(required=False)
    
    short_description = fields.Str(required=False)
    
    rating = fields.Float(required=False)
    
    is_set = fields.Boolean(required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
    images = fields.List(fields.Dict(required=False), required=False)
    
    image_nature = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    grouped_attributes = fields.Dict(required=False)
    
    media = fields.List(fields.Dict(required=False), required=False)
    
    country_of_origin = fields.Str(required=False)
    
    brand_uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    rating_count = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    template_tag = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    hsn_code = fields.Int(required=False)
    

