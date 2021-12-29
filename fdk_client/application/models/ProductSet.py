"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductSetDistribution import ProductSetDistribution




class ProductSet(BaseSchema):
    # Catalog swagger.json

    
    size_distribution = fields.Nested(ProductSetDistribution, required=False)
    
    quantity = fields.Int(required=False)
    

