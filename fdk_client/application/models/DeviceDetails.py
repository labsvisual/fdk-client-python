"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class DeviceDetails(BaseSchema):
    # Payment swagger.json

    
    device_make = fields.Str(required=False)
    
    os = fields.Str(required=False)
    
    identifier_type = fields.Str(required=False)
    
    identification_number = fields.Str(required=False)
    
    device_model = fields.Str(required=False)
    
    os_version = fields.Str(required=False)
    
    device_type = fields.Str(required=False)
    

