"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .LocationDetails import LocationDetails






















class GetTatProductResponse(BaseSchema):
    # Logistic swagger.json

    
    location_details = fields.List(fields.Nested(LocationDetails, required=False), required=False)
    
    request_uuid = fields.Str(required=False)
    
    error = fields.Dict(required=False)
    
    to_city = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    to_pincode = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    stormbreaker_uuid = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    identifier = fields.Str(required=False)
    
    journey = fields.Str(required=False)
    

