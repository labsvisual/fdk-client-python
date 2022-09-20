"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


























class LimitedProductData(BaseSchema):
    # Catalog swagger.json

    
    images = fields.List(fields.Str(required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    identifier = fields.Dict(required=False)
    
    price = fields.Dict(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    short_description = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    country_of_origin = fields.Str(required=False)
    

