"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class CreateQNARequest(BaseSchema):
    # Feedback swagger.json

    
    choices = fields.List(fields.Str(required=False), required=False)
    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    max_len = fields.Int(required=False)
    
    sort_priority = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    text = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

