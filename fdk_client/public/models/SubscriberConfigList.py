"""Public Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SubscriberResponse import SubscriberResponse

from .Page import Page


class SubscriberConfigList(BaseSchema):
    # Webhook swagger.json

    
    items = fields.List(fields.Nested(SubscriberResponse, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

