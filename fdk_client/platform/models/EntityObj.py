"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class EntityObj(BaseSchema):
    # AuditTrail swagger.json

    
    id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    entity_details = fields.Dict(required=False)
    

