"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ReviewFacet import ReviewFacet



from .Page import Page

from .SortMethod import SortMethod


class GetReviewResponse(BaseSchema):
    # Feedback swagger.json

    
    facets = fields.List(fields.Nested(ReviewFacet, required=False), required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    sort = fields.List(fields.Nested(SortMethod, required=False), required=False)
    

