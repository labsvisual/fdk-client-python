"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ImageUrls import ImageUrls





from .Media1 import Media1







from .Action import Action
























class GetCollectionDetailNest(BaseSchema):
    # Catalog swagger.json

    
    banners = fields.Nested(ImageUrls, required=False)
    
    _schedule = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    logo = fields.Nested(Media1, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    action = fields.Nested(Action, required=False)
    
    uid = fields.Str(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    cron = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    badge = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    

