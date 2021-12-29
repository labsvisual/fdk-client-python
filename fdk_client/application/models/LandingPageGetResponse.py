"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .LandingPageSchema import LandingPageSchema

from .Page import Page


class LandingPageGetResponse(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(LandingPageSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

