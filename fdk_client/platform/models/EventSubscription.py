"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EventSubscriptionTemplate import EventSubscriptionTemplate


















class EventSubscription(BaseSchema):
    # Communication swagger.json

    
    template = fields.Nested(EventSubscriptionTemplate, required=False)
    
    is_default = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    event = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    

