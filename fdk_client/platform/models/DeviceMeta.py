"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class DeviceMeta(BaseSchema):
    # Feedback swagger.json

    
    app_version = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    

