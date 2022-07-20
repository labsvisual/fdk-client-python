"""Public Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class SubscriberEvent(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    subscriber_id = fields.Int(required=False)
    
    event_id = fields.Int(required=False)
    
    created_date = fields.Str(required=False)
    

