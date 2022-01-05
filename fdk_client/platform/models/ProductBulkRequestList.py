"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductBulkRequest import ProductBulkRequest

from .Page import Page


class ProductBulkRequestList(BaseSchema):
    # Catalog swagger.json

    
    items = fields.Nested(ProductBulkRequest, required=False)
    
    page = fields.Nested(Page, required=False)
    

