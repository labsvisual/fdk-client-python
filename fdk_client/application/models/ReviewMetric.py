"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .RatingMetric import RatingMetric



from .Entity import Entity









from .RatingMetric import RatingMetric




class ReviewMetric(BaseSchema):
    # Feedback swagger.json

    
    attribute_metric = fields.List(fields.Nested(RatingMetric, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    entity = fields.Nested(Entity, required=False)
    
    id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    rating_avg = fields.Float(required=False)
    
    rating_count = fields.Int(required=False)
    
    rating_metric = fields.List(fields.Nested(RatingMetric, required=False), required=False)
    
    review_count = fields.Int(required=False)
    

