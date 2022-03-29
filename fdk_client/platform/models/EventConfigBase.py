"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class EventConfigBase(BaseSchema):
    # Webhook swagger.json

    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    event_category = fields.Str(required=False)
    
    version = fields.Str(required=False)
    

