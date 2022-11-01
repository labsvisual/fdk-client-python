"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .SeoDetail import SeoDetail









from .CollectionSchedule import CollectionSchedule









from .CollectionBanner import CollectionBanner









from .CollectionBadge import CollectionBadge

from .CollectionImage import CollectionImage





from .UserInfo import UserInfo



from .CollectionQuery import CollectionQuery


class UpdateCollection(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Dict(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    description = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    published = fields.Boolean(required=False)
    
    sort_on = fields.Str(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    is_active = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    

