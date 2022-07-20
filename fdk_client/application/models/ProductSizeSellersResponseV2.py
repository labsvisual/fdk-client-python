"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductSizePriceResponseV2 import ProductSizePriceResponseV2

from .Page import Page

from .ProductSizeSellerFilterSchemaV2 import ProductSizeSellerFilterSchemaV2


class ProductSizeSellersResponseV2(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductSizePriceResponseV2, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    sort_on = fields.List(fields.Nested(ProductSizeSellerFilterSchemaV2, required=False), required=False)
    

