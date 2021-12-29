"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SystemSmsTemplate import SystemSmsTemplate

from .Page import Page


class SystemSmsTemplates(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(SystemSmsTemplate, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

