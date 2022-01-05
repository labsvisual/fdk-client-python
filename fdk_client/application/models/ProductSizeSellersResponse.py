"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Page import Page

from .ProductSizePriceResponse import ProductSizePriceResponse

from .ProductSizeSellerFilter import ProductSizeSellerFilter


class ProductSizeSellersResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(ProductSizePriceResponse, required=False), required=False)
    
    sort_on = fields.List(fields.Nested(ProductSizeSellerFilter, required=False), required=False)
    

