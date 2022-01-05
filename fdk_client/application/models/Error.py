"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class Error(BaseSchema):
    # Rewards swagger.json

    
    code = fields.Int(required=False)
    
    exception = fields.Str(required=False)
    
    info = fields.Str(required=False)
    
    message = fields.Str(required=False)
    

