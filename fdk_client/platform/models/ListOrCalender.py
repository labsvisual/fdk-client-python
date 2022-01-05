"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DiscountJob import DiscountJob

from .Page import Page


class ListOrCalender(BaseSchema):
    # Discount swagger.json

    
    items = fields.List(fields.Nested(DiscountJob, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

