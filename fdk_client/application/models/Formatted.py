"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Formatted(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    

