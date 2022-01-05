"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SmsProvider import SmsProvider

from .Page import Page


class SmsProviders(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(SmsProvider, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

