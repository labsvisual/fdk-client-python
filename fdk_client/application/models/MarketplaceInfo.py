"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class MarketplaceInfo(BaseSchema):
    # Payment swagger.json

    
    date_of_joining = fields.Str(required=False)
    
    membership_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

