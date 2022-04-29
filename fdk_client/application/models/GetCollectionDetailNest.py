"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema























from .ImageUrls import ImageUrls



from .ProductListingAction import ProductListingAction









from .Media import Media


class GetCollectionDetailNest(BaseSchema):
    # Catalog swagger.json

    
    query = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    _schedule = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    cron = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    badge = fields.Dict(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    name = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    

