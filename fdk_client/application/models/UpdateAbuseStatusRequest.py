"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class UpdateAbuseStatusRequest(BaseSchema):
    # Feedback swagger.json

    
    abusive = fields.Boolean(required=False)
    
    active = fields.Boolean(required=False)
    
    approve = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    

