"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class EntityTypeObj(BaseSchema):
    # AuditTrail swagger.json

    
    entity_value = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    

