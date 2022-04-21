"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .CollectionBanner import CollectionBanner



from .UserInfo import UserInfo

from .UserInfo import UserInfo



















from .Schedule import Schedule



from .CollectionImage import CollectionImage



from .SeoDetail import SeoDetail



from .CollectionBadge import CollectionBadge


class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    published = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    query = fields.Dict(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    type = fields.Str(required=False)
    
    sort_on = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    is_active = fields.Boolean(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    

