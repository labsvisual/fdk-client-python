"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class TextDetector(BaseSchema):
    # Feedback swagger.json

    
    confidence = fields.Float(required=False)
    
    text = fields.Str(required=False)
    
    text_class = fields.Str(required=False)
    
    text_type = fields.Str(required=False)
    

