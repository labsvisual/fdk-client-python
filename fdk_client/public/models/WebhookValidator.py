"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class WebhookValidator:
    
    class fetchAllWebhookEvents(BaseSchema):
        
        pass 
    
    class queryWebhookEventDetails(BaseSchema):
        
        pass 
    