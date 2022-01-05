"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BrandStoreInfo import BrandStoreInfo

from .Page import Page


class StoreByBrandsResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(BrandStoreInfo, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

