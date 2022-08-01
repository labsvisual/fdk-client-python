"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductListingDetail import ProductListingDetail

from .ProductFilters import ProductFilters

from .Page import Page

from .ProductSortOn import ProductSortOn


class GetCollectionItemsResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    
    filters = fields.List(fields.Nested(ProductFilters, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    

