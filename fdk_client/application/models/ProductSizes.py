"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductSizeStores import ProductSizeStores





from .SizeChart import SizeChart

from .ProductSize import ProductSize

from .ProductListingPrice import ProductListingPrice


class ProductSizes(BaseSchema):
    # Catalog swagger.json

    
    stores = fields.Nested(ProductSizeStores, required=False)
    
    sellable = fields.Boolean(required=False)
    
    discount = fields.Str(required=False)
    
    size_chart = fields.Nested(SizeChart, required=False)
    
    sizes = fields.List(fields.Nested(ProductSize, required=False), required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    

