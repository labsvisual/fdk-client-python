"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Images import Images








class Information(BaseSchema):
    # Theme swagger.json

    
    images = fields.Nested(Images, required=False)
    
    features = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    

