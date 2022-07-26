"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

















from .ImageUrls import ImageUrls















from .BannerImage import BannerImage


class CollectionCreateResponse(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    cron = fields.Dict(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    meta = fields.Dict(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    query = fields.Dict(required=False)
    
    _schedule = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    badge = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Nested(BannerImage, required=False)
    

