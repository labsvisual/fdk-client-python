"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


























class AddProductCart(BaseSchema):
    # Cart swagger.json

    
    extra_meta = fields.Dict(required=False)
    
    article_assignment = fields.Dict(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    store_id = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    
    seller_id = fields.Int(required=False)
    
    item_size = fields.Str(required=False)
    
    article_id = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    pos = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    

