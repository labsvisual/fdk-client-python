"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Media import Media

from .ProductListingAction import ProductListingAction




class AutocompleteItem(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    type = fields.Str(required=False)
    

