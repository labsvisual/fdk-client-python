"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class LoyaltyPointsConfig(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    
    auto_apply = fields.Boolean(required=False)
    

