"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SlideshowSchema import SlideshowSchema




class Slideshow(BaseSchema):
    # Content swagger.json

    
    data = fields.Nested(SlideshowSchema, required=False)
    
    success = fields.Boolean(required=False)
    

