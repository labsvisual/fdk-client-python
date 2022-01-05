"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class EventProcessedStatus(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    subscriber_id = fields.Str(required=False)
    
    attempt = fields.Int(required=False)
    
    response_code = fields.Str(required=False)
    
    response_message = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    processed_on = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    

