"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Media import Media

from .Media import Media


class ImageUrls(BaseSchema):
    # Catalog swagger.json

    
    landscape = fields.Nested(Media, required=False)
    
    portrait = fields.Nested(Media, required=False)
    

