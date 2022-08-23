"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .CollectionQuery import CollectionQuery

from .ImageUrls import ImageUrls





















from .BannerImage import BannerImage








class CollectionCreateResponse(BaseSchema):
    # Catalog swagger.json

    
    app_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    _schedule = fields.Dict(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    cron = fields.Dict(required=False)
    
    sort_on = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    badge = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    logo = fields.Nested(BannerImage, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    name = fields.Str(required=False)
    

