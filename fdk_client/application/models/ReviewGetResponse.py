"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ReviewFacet import ReviewFacet

from .CustomerReview import CustomerReview

from .Page import Page

from .SortMethod import SortMethod


class ReviewGetResponse(BaseSchema):
    # Feedback swagger.json

    
    facets = fields.List(fields.Nested(ReviewFacet, required=False), required=False)
    
    items = fields.List(fields.Nested(CustomerReview, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    sort = fields.List(fields.Nested(SortMethod, required=False), required=False)
    

