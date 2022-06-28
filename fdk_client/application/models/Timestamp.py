"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class Timestamp(BaseSchema):
    # Order swagger.json

    
    show_promise = fields.Boolean(required=False)
    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    

