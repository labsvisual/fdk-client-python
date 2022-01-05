"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PageSchema import PageSchema

from .Page import Page


class PageGetResponse(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(PageSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

