"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductSizeSellerFilterSchemaV2 import ProductSizeSellerFilterSchemaV2

from .ProductSizePriceResponseV2 import ProductSizePriceResponseV2

from .Page import Page


class ProductSizeSellersResponseV2(BaseSchema):
    # Catalog swagger.json

    
    sort_on = fields.List(fields.Nested(ProductSizeSellerFilterSchemaV2, required=False), required=False)
    
    items = fields.List(fields.Nested(ProductSizePriceResponseV2, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

