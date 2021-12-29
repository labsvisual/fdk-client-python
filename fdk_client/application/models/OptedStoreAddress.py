"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .StoreLatLong import StoreLatLong










class OptedStoreAddress(BaseSchema):
    # Configuration swagger.json

    
    state = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    lat_long = fields.Nested(StoreLatLong, required=False)
    
    address2 = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    country = fields.Str(required=False)
    
    city = fields.Str(required=False)
    

