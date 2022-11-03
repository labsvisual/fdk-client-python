"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class CatalogInsightItem(BaseSchema):
    # Catalog swagger.json

    
    out_of_stock_count = fields.Int(required=False)
    
    sellable_count = fields.Int(required=False)
    
    count = fields.Int(required=False)
    

