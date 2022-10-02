"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BannerImage import BannerImage

from .BannerImage import BannerImage


class ImageUrls(BaseSchema):
    # Catalog swagger.json

    
    portrait = fields.Nested(BannerImage, required=False)
    
    landscape = fields.Nested(BannerImage, required=False)
    

