"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EpaylaterBannerData import EpaylaterBannerData




class EpaylaterBannerResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(EpaylaterBannerData, required=False)
    
    success = fields.Boolean(required=False)
    

