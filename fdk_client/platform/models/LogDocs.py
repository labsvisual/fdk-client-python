"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EntityObj import EntityObj

from .Modifier import Modifier

from .DeviceInfo import DeviceInfo

from .Location import Location














class LogDocs(BaseSchema):
    # AuditTrail swagger.json

    
    entity = fields.Nested(EntityObj, required=False)
    
    modifier = fields.Nested(Modifier, required=False)
    
    device_info = fields.Nested(DeviceInfo, required=False)
    
    location = fields.Nested(Location, required=False)
    
    _id = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    sessions = fields.Str(required=False)
    
    date = fields.Str(required=False)
    
    logs = fields.Dict(required=False)
    

