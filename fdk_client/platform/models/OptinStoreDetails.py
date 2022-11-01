"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .StoreDetail import StoreDetail

from .Page import Page


class OptinStoreDetails(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(StoreDetail, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

