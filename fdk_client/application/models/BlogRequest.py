"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Author import Author

from .ResourceContent import ResourceContent

from .Asset import Asset











from .SEO import SEO

from .CronSchedule import CronSchedule


class BlogRequest(BaseSchema):
    # Content swagger.json

    
    application = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    author = fields.Nested(Author, required=False)
    
    content = fields.List(fields.Nested(ResourceContent, required=False), required=False)
    
    feature_image = fields.Nested(Asset, required=False)
    
    published = fields.Boolean(required=False)
    
    reading_time = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    title = fields.Str(required=False)
    
    seo = fields.Nested(SEO, required=False)
    
    _schedule = fields.Nested(CronSchedule, required=False)
    

