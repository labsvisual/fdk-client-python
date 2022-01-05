"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class PointsResponse(BaseSchema):
    # Rewards swagger.json

    
    points = fields.Float(required=False)
    

