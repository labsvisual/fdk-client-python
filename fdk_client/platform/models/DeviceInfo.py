"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class DeviceInfo(BaseSchema):
    # AuditTrail swagger.json

    
    user_agent = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    

