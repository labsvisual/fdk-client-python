"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Page import Page


class GetResponse(BaseSchema):
    # Feedback swagger.json

    
    data = fields.Dict(required=False)
    
    page = fields.Nested(Page, required=False)
    

