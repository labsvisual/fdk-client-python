"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SlideshowSchema import SlideshowSchema

from .Page import Page


class SlideshowGetResponse(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(SlideshowSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

