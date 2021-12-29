"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class EventSubscriptionTemplateEmail(BaseSchema):
    # Communication swagger.json

    
    subscribed = fields.Boolean(required=False)
    
    template = fields.Str(required=False)
    

