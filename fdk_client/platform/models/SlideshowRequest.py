"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ConfigurationSchema import ConfigurationSchema

from .SlideshowMedia import SlideshowMedia




class SlideshowRequest(BaseSchema):
    # Content swagger.json

    
    slug = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    configuration = fields.Nested(ConfigurationSchema, required=False)
    
    media = fields.Nested(SlideshowMedia, required=False)
    
    active = fields.Boolean(required=False)
    

