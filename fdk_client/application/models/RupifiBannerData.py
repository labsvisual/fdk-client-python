"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class RupifiBannerData(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    kyc_url = fields.Str(required=False)
    

