"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class CurrentStatus(BaseSchema):
    # Order swagger.json

    
    updated_at = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    

