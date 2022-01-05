"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Audience import Audience

from .Page import Page


class Audiences(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(Audience, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

