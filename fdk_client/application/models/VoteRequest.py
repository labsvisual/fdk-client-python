"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class VoteRequest(BaseSchema):
    # Feedback swagger.json

    
    action = fields.Str(required=False)
    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    ref_id = fields.Str(required=False)
    
    ref_type = fields.Str(required=False)
    

