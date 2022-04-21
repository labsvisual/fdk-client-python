"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ProductSize import ProductSize

from .ProductListingPrice import ProductListingPrice

from .SizeChart import SizeChart

from .ProductSizeStores import ProductSizeStores


class ProductSizes(BaseSchema):
    # Catalog swagger.json

    
    discount = fields.Str(required=False)
    
    sellable = fields.Boolean(required=False)
    
    sizes = fields.List(fields.Nested(ProductSize, required=False), required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    size_chart = fields.Nested(SizeChart, required=False)
    
    stores = fields.Nested(ProductSizeStores, required=False)
    

