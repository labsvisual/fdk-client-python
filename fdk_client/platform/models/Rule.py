"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class Rule(BaseSchema):
    # Cart swagger.json

    
    discount_qty = fields.Float(required=False)
    
    max = fields.Float(required=False)
    
    key = fields.Float(required=False)
    
    min = fields.Float(required=False)
    
    value = fields.Float(required=False)
    

