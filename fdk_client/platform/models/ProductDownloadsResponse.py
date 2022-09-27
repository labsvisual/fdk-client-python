"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductDownloadsItems import ProductDownloadsItems

from .Page import Page


class ProductDownloadsResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.Nested(ProductDownloadsItems, required=False)
    
    page = fields.Nested(Page, required=False)
    

