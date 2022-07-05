"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

















from .GeoLocation import GeoLocation




























class Address(BaseSchema):
    # Cart swagger.json

    
    checkout_mode = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    phone = fields.Str(required=False)
    
    area_code = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    is_default_address = fields.Boolean(required=False)
    
    email = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    geo_location = fields.Nested(GeoLocation, required=False)
    
    address_type = fields.Str(required=False)
    
    google_map_point = fields.Dict(required=False)
    
    country_code = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    landmark = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    city = fields.Str(required=False)
    

