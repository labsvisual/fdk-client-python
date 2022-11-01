"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ProductStockUnitPriceV2(BaseSchema):
    # Catalog swagger.json

    
    currency_symbol = fields.Str(required=False)
    
    unit = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
    price = fields.Float(required=False)
    

