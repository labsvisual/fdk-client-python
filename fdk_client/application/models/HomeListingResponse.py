"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductListingDetail import ProductListingDetail

from .Page import Page


class HomeListingResponse(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

