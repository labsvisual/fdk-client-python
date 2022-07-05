"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductPrice import ProductPrice

from .ProductPrice import ProductPrice


class ProductPriceInfo(BaseSchema):
    # Cart swagger.json

    
    base = fields.Nested(ProductPrice, required=False)
    
    converted = fields.Nested(ProductPrice, required=False)
    

