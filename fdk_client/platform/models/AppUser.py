"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class AppUser(BaseSchema):
    # Rewards swagger.json

    
    _id = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    application_id = fields.Str(required=False)
    
    block_reason = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    

