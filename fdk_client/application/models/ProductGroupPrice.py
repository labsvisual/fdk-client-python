"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class ProductGroupPrice(BaseSchema):
    # Catalog swagger.json

    
    min_effective = fields.Float(required=False)
    
    max_effective = fields.Float(required=False)
    
    max_marked = fields.Float(required=False)
    
    currency = fields.Raw(required=False)
    
    min_marked = fields.Float(required=False)
    

