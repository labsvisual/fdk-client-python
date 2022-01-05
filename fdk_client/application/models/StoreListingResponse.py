"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Store1 import Store1

from .Page import Page


class StoreListingResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(Store1, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

