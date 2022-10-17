"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema















from .CartProductIdentifer import CartProductIdentifer


class UpdateProductCart(BaseSchema):
    # Cart swagger.json

    
    item_index = fields.Int(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    item_size = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    article_id = fields.Str(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    

