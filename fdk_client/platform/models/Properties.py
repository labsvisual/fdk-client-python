"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






























































class Properties(BaseSchema):
    # Catalog swagger.json

    
    trader = fields.Dict(required=False)
    
    category_slug = fields.Dict(required=False)
    
    media = fields.Dict(required=False)
    
    hsn_code = fields.Dict(required=False)
    
    currency = fields.Dict(required=False)
    
    tags = fields.Dict(required=False)
    
    short_description = fields.Dict(required=False)
    
    is_active = fields.Dict(required=False)
    
    moq = fields.Dict(required=False)
    
    no_of_boxes = fields.Dict(required=False)
    
    description = fields.Dict(required=False)
    
    multi_size = fields.Dict(required=False)
    
    custom_order = fields.Dict(required=False)
    
    highlights = fields.Dict(required=False)
    
    name = fields.Dict(required=False)
    
    is_dependent = fields.Dict(required=False)
    
    return_config = fields.Dict(required=False)
    
    size_guide = fields.Dict(required=False)
    
    brand_uid = fields.Dict(required=False)
    
    teaser_tag = fields.Dict(required=False)
    
    country_of_origin = fields.Dict(required=False)
    
    sizes = fields.Dict(required=False)
    
    item_type = fields.Dict(required=False)
    
    command = fields.Dict(required=False)
    
    variants = fields.Dict(required=False)
    
    slug = fields.Dict(required=False)
    
    product_group_tag = fields.Dict(required=False)
    
    trader_type = fields.Dict(required=False)
    
    product_publish = fields.Dict(required=False)
    
    item_code = fields.Dict(required=False)
    

