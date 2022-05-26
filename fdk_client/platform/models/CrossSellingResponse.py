"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CrossSellingData import CrossSellingData

from .CatalogInsightBrand import CatalogInsightBrand


class CrossSellingResponse(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(CrossSellingData, required=False)
    
    brand_distribution = fields.Nested(CatalogInsightBrand, required=False)
    

