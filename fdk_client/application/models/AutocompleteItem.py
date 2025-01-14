"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ProductListingAction import ProductListingAction

from .Media import Media




class AutocompleteItem(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    logo = fields.Nested(Media, required=False)
    
    display = fields.Str(required=False)
    

