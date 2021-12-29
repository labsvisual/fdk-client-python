"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .CreatedBySchema import CreatedBySchema

from .DateMeta import DateMeta



from .Asset import Asset



from .ScheduleSchema import ScheduleSchema

















from .SEO import SEO






class PageSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    component_ids = fields.List(fields.Str(required=False), required=False)
    
    content = fields.List(fields.Dict(required=False), required=False)
    
    content_path = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedBySchema, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    description = fields.Str(required=False)
    
    feature_image = fields.Nested(Asset, required=False)
    
    page_meta = fields.List(fields.Dict(required=False), required=False)
    
    _schedule = fields.Nested(ScheduleSchema, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    orientation = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    title = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    seo = fields.Nested(SEO, required=False)
    
    visibility = fields.Dict(required=False)
    
    archived = fields.Boolean(required=False)
    

