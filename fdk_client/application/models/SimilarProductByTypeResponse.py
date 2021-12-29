"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductSimilarItem import ProductSimilarItem


class SimilarProductByTypeResponse(BaseSchema):
    # Catalog swagger.json

    
    similars = fields.Nested(ProductSimilarItem, required=False)
    

