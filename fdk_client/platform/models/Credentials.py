"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Ios import Ios

from .Android import Android










class Credentials(BaseSchema):
    # Configuration swagger.json

    
    ios = fields.Nested(Ios, required=False)
    
    android = fields.Nested(Android, required=False)
    
    project_id = fields.Str(required=False)
    
    gcm_sender_id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    api_key = fields.Str(required=False)
    

