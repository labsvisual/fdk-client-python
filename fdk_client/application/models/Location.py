"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .GeoLoc import GeoLoc






class Location(BaseSchema):
    # Feedback swagger.json

    
    country_code = fields.Str(required=False)
    
    flag_url = fields.Str(required=False)
    
    geo_loc = fields.Nested(GeoLoc, required=False)
    
    name = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    

