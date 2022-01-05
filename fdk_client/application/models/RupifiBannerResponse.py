"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .RupifiBannerData import RupifiBannerData




class RupifiBannerResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(RupifiBannerData, required=False)
    
    success = fields.Boolean(required=False)
    

