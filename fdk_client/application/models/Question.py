"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class Question(BaseSchema):
    # Feedback swagger.json

    
    choices = fields.List(fields.Str(required=False), required=False)
    
    max_len = fields.Int(required=False)
    
    text = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

