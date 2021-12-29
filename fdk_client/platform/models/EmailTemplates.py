"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EmailTemplate import EmailTemplate

from .Page import Page


class EmailTemplates(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(EmailTemplate, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

