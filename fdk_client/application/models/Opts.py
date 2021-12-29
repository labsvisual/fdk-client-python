"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class Opts(BaseSchema):
    # FileStorage swagger.json

    
    attempts = fields.Int(required=False)
    
    timestamp = fields.Int(required=False)
    
    delay = fields.Int(required=False)
    

