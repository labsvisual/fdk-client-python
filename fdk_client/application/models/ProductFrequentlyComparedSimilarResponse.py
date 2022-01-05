"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductCompareResponse import ProductCompareResponse


class ProductFrequentlyComparedSimilarResponse(BaseSchema):
    # Catalog swagger.json

    
    similars = fields.Nested(ProductCompareResponse, required=False)
    

