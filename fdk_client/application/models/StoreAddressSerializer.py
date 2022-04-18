"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




















class StoreAddressSerializer(BaseSchema):
    # Catalog swagger.json

    
    address1 = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    latitude = fields.Float(required=False)
    
    country = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    

