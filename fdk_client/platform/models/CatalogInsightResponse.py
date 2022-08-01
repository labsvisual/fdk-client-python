"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CatalogInsightItem import CatalogInsightItem

from .CatalogInsightBrand import CatalogInsightBrand


class CatalogInsightResponse(BaseSchema):
    # Catalog swagger.json

    
    item = fields.Nested(CatalogInsightItem, required=False)
    
    brand_distribution = fields.Nested(CatalogInsightBrand, required=False)
    

