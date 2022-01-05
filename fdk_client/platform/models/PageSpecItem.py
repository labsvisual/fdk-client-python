"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .PageSpecParam import PageSpecParam

from .PageSpecParam import PageSpecParam


class PageSpecItem(BaseSchema):
    # Content swagger.json

    
    page_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    params = fields.List(fields.Nested(PageSpecParam, required=False), required=False)
    
    query = fields.List(fields.Nested(PageSpecParam, required=False), required=False)
    

