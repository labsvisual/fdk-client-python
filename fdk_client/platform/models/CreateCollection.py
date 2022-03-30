"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .UserInfo import UserInfo













from .CollectionBadge import CollectionBadge



from .Schedule import Schedule





from .SeoDetail import SeoDetail



from .CollectionImage import CollectionImage





from .CollectionBanner import CollectionBanner



from .UserInfo import UserInfo




class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    slug = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    sort_on = fields.Str(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    is_visible = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    _locale_language = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    query = fields.Dict(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    

