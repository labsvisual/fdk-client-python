"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .PageNumber import PageNumber


class NumberGetResponse(BaseSchema):
    # Feedback swagger.json

    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.Nested(PageNumber, required=False)
    

