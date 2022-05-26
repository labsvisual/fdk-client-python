"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BrandItem import BrandItem

from .Page import Page


class BrandListingResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(BrandItem, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

