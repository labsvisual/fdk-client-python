"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductSortOn import ProductSortOn

from .ProductFilters import ProductFilters

from .ProductListingDetail import ProductListingDetail

from .Page import Page


class ProductListingResponse(BaseSchema):
    # Catalog swagger.json

    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    
    filters = fields.List(fields.Nested(ProductFilters, required=False), required=False)
    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

