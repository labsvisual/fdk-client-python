"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductListingActionPage import ProductListingActionPage


class ProductListingAction(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    page = fields.Nested(ProductListingActionPage, required=False)
    

