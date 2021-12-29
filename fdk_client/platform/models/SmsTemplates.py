"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SmsTemplate import SmsTemplate

from .Page import Page


class SmsTemplates(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(SmsTemplate, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

