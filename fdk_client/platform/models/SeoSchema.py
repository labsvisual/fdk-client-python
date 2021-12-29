"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .Detail import Detail






class SeoSchema(BaseSchema):
    # Content swagger.json

    
    app = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    robots_txt = fields.Str(required=False)
    
    sitemap_enabled = fields.Boolean(required=False)
    
    custom_meta_tags = fields.List(fields.Dict(required=False), required=False)
    
    details = fields.Nested(Detail, required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    

