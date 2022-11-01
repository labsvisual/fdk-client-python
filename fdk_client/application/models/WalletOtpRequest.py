"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class WalletOtpRequest(BaseSchema):
    # Payment swagger.json

    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    

