"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Attribute import Attribute

from .Page import Page


class AttributeResponse(BaseSchema):
    # Feedback swagger.json

    
    items = fields.List(fields.Nested(Attribute, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

