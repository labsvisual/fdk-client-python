"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class UpdateVoteRequest(BaseSchema):
    # Feedback swagger.json

    
    action = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    ref_id = fields.Str(required=False)
    
    ref_type = fields.Str(required=False)
    

