"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AutoDetectors import AutoDetectors



from .DeviceMeta import DeviceMeta

from .ProductEntity import ProductEntity



from .LocationMeta import LocationMeta





from .ReviewRating import ReviewRating

from .Review import Review



from .State import State

from .TagMeta import TagMeta

from .Template import Template

from .VoteCount import VoteCount


class CustomerReview(BaseSchema):
    # Feedback swagger.json

    
    auto_detectors = fields.Nested(AutoDetectors, required=False)
    
    created_on = fields.Str(required=False)
    
    device_meta = fields.Nested(DeviceMeta, required=False)
    
    entity = fields.Nested(ProductEntity, required=False)
    
    id = fields.Str(required=False)
    
    location_meta = fields.Nested(LocationMeta, required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    rating = fields.Nested(ReviewRating, required=False)
    
    review = fields.Nested(Review, required=False)
    
    slug = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    tags = fields.List(fields.Nested(TagMeta, required=False), required=False)
    
    template = fields.Nested(Template, required=False)
    
    vote_count = fields.Nested(VoteCount, required=False)
    

