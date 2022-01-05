"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SystemEmailTemplate import SystemEmailTemplate

from .Page import Page


class SystemEmailTemplates(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(SystemEmailTemplate, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

