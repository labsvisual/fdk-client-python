"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .Media1 import Media1

from .CollectionQuery import CollectionQuery





from .ImageUrls import ImageUrls















from .Action import Action








class GetCollectionDetailNest(BaseSchema):
    # Catalog swagger.json

    
    cron = fields.Dict(required=False)
    
    badge = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Nested(Media1, required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    _schedule = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    priority = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

