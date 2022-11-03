"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class ProductBundleItem(BaseSchema):
    # Catalog swagger.json

    
    min_quantity = fields.Int(required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    max_quantity = fields.Int(required=False)
    
    product_uid = fields.Int(required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    auto_select = fields.Boolean(required=False)
    

