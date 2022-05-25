"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CollectionBadge import CollectionBadge









from .Schedule import Schedule



from .UserInfo import UserInfo











from .CollectionBanner import CollectionBanner

from .SeoDetail import SeoDetail









from .UserInfo import UserInfo

from .CollectionImage import CollectionImage








class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    badge = fields.Nested(CollectionBadge, required=False)
    
    app_id = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    
    published = fields.Boolean(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    description = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    sort_on = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    meta = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    _locale_language = fields.Dict(required=False)
    

