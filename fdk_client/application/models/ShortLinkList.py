"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ShortLinkRes import ShortLinkRes

from .Page import Page


class ShortLinkList(BaseSchema):
    # Share swagger.json

    
    items = fields.List(fields.Nested(ShortLinkRes, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

