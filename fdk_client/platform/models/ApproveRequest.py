"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ApproveRequest(BaseSchema):
    # Feedback swagger.json

    
    approve = fields.Boolean(required=False)
    
    entity_type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    

