"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


































class PickupStoreDetail(BaseSchema):
    # PosCart swagger.json

    
    name = fields.Str(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    phone = fields.Str(required=False)
    
    area_code = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    address = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    

