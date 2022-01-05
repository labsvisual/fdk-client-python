"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EventSubscription import EventSubscription

from .Page import Page


class EventSubscriptions(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(EventSubscription, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

