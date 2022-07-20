"""Public Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .Association import Association







from .AuthMeta import AuthMeta





from .EventConfig import EventConfig


class SubscriberResponse(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    webhook_url = fields.Str(required=False)
    
    association = fields.Nested(Association, required=False)
    
    custom_headers = fields.Dict(required=False)
    
    email_id = fields.Str(required=False)
    
    status = fields.Str(required=False, validate=OneOf([val.value for val in SubscriberStatus.__members__.values()]))
    
    auth_meta = fields.Nested(AuthMeta, required=False)
    
    created_on = fields.Str(required=False)
    
    updated_on = fields.Str(required=False)
    
    event_configs = fields.List(fields.Nested(EventConfig, required=False), required=False)
    

