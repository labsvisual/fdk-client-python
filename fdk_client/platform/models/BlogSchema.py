"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .Author import Author

from .ResourceContent import ResourceContent

from .Asset import Asset









from .SEO import SEO

from .CronSchedule import CronSchedule



from .DateMeta import DateMeta


class BlogSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    application = fields.Str(required=False)
    
    archived = fields.Boolean(required=False)
    
    author = fields.Nested(Author, required=False)
    
    content = fields.List(fields.Nested(ResourceContent, required=False), required=False)
    
    feature_image = fields.Nested(Asset, required=False)
    
    published = fields.Boolean(required=False)
    
    reading_time = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(SEO, required=False)
    
    _schedule = fields.Nested(CronSchedule, required=False)
    
    title = fields.Str(required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    

