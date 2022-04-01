"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class EntityObject(BaseSchema):
    # AuditTrail swagger.json

    
    type = fields.Str(required=False)
    
    action = fields.Str(required=False)
    

