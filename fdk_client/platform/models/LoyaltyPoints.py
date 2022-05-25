"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class LoyaltyPoints(BaseSchema):
    # Cart swagger.json

    
    description = fields.Str(required=False)
    
    applicable = fields.Float(required=False)
    
    total = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    

