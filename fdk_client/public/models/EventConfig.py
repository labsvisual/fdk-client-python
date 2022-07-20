"""Public Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class EventConfig(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    event_category = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    

