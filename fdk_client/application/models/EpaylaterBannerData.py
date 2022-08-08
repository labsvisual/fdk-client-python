"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class EpaylaterBannerData(BaseSchema):
    # Payment swagger.json

    
    display = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    status = fields.Str(required=False)
    

