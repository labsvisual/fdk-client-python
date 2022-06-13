"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema















from .CollectionBadge import CollectionBadge

from .Schedule import Schedule





from .CollectionImage import CollectionImage



from .SeoDetail import SeoDetail







from .UserInfo import UserInfo









from .UserInfo import UserInfo

from .CollectionBanner import CollectionBanner


class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    is_visible = fields.Boolean(required=False)
    
    sort_on = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    app_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    published = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    

