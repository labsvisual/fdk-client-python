"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .ImageUrls import ImageUrls









from .Media import Media


















class CollectionDetailResponse(BaseSchema):
    # Catalog swagger.json

    
    allow_sort = fields.Boolean(required=False)
    
    cron = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    type = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    query = fields.Dict(required=False)
    
    _schedule = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    badge = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    

