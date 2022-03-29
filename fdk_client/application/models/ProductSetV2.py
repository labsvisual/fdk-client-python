"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductSetDistributionV2 import ProductSetDistributionV2




class ProductSetV2(BaseSchema):
    # Catalog swagger.json

    
    size_distribution = fields.Nested(ProductSetDistributionV2, required=False)
    
    quantity = fields.Int(required=False)
    

