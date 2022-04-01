"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CreateLogResponse(BaseSchema):
    # AuditTrail swagger.json

    
    message = fields.Str(required=False)
    
    internal_message = fields.Str(required=False)
    

