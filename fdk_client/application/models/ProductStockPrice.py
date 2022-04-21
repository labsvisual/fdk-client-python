"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ProductStockPrice(BaseSchema):
    # Catalog swagger.json

    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    

