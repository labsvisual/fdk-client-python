"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .StoreAddressJson import StoreAddressJson






















class RtoAddress(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    phone = fields.Str(required=False)
    
    location_type = fields.Str(required=False)
    
    store_address_json = fields.Nested(StoreAddressJson, required=False)
    
    code = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    contact_person = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    store_email = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    

