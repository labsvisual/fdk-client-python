"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Media import Media



from .ImageUrls import ImageUrls


class BrandDetailResponse(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    name = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    

