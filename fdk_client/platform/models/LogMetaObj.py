"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .EntityObject import EntityObject






class LogMetaObj(BaseSchema):
    # AuditTrail swagger.json

    
    modifier = fields.Dict(required=False)
    
    application = fields.Str(required=False)
    
    entity = fields.Nested(EntityObject, required=False)
    
    device_info = fields.Dict(required=False)
    
    location = fields.Dict(required=False)
    

