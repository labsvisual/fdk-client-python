"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CatalogInsightBrand import CatalogInsightBrand

from .CrossSellingData import CrossSellingData


class CrossSellingResponse(BaseSchema):
    # Catalog swagger.json

    
    brand_distribution = fields.Nested(CatalogInsightBrand, required=False)
    
    data = fields.Nested(CrossSellingData, required=False)
    

