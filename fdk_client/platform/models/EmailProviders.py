"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EmailProvider import EmailProvider

from .Page import Page


class EmailProviders(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(EmailProvider, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

