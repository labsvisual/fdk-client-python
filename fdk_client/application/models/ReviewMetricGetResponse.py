"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ReviewMetric import ReviewMetric

from .Page import Page


class ReviewMetricGetResponse(BaseSchema):
    # Feedback swagger.json

    
    items = fields.List(fields.Nested(ReviewMetric, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

