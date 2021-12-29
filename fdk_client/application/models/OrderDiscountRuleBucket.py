"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class OrderDiscountRuleBucket(BaseSchema):
    # Rewards swagger.json

    
    high = fields.Float(required=False)
    
    low = fields.Float(required=False)
    
    max = fields.Float(required=False)
    
    value = fields.Float(required=False)
    
    value_type = fields.Str(required=False)
    

