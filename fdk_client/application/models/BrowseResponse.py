"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DbRecord import DbRecord

from .Page import Page


class BrowseResponse(BaseSchema):
    # FileStorage swagger.json

    
    items = fields.List(fields.Nested(DbRecord, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

