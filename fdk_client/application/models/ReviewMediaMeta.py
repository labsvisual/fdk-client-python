"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ReviewMediaMeta(BaseSchema):
    # Feedback swagger.json

    
    max_count = fields.Float(required=False)
    
    size = fields.Float(required=False)
    
    type = fields.Str(required=False)
    

