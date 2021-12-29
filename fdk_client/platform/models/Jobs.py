"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Job import Job

from .Page import Page


class Jobs(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(Job, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

