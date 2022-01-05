"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EventSubscriptionTemplateSms import EventSubscriptionTemplateSms

from .EventSubscriptionTemplateEmail import EventSubscriptionTemplateEmail


class EventSubscriptionTemplate(BaseSchema):
    # Communication swagger.json

    
    sms = fields.Nested(EventSubscriptionTemplateSms, required=False)
    
    email = fields.Nested(EventSubscriptionTemplateEmail, required=False)
    

