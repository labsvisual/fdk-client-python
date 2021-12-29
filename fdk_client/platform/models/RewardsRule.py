"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class RewardsRule(BaseSchema):
    # Rewards swagger.json

    
    amount = fields.Float(required=False)
    

