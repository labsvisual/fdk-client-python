"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class EpaylaterBannerData(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    display = fields.Boolean(required=False)
    

