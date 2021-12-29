"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class RewardsArticle(BaseSchema):
    # Rewards swagger.json

    
    id = fields.Str(required=False)
    
    points = fields.Float(required=False)
    
    price = fields.Float(required=False)
    

