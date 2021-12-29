"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Template import Template

from .Page import Page


class TemplateGetResponse(BaseSchema):
    # Feedback swagger.json

    
    items = fields.List(fields.Nested(Template, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

