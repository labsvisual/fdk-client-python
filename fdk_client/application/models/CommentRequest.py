"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class CommentRequest(BaseSchema):
    # Feedback swagger.json

    
    comment = fields.List(fields.Str(required=False), required=False)
    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    

