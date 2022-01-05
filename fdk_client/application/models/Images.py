"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class Images(BaseSchema):
    # Theme swagger.json

    
    desktop = fields.List(fields.Str(required=False), required=False)
    
    android = fields.List(fields.Str(required=False), required=False)
    
    ios = fields.List(fields.Str(required=False), required=False)
    
    thumbnail = fields.List(fields.Str(required=False), required=False)
    

