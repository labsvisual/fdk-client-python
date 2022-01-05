"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class GeoLocation(BaseSchema):
    # Cart swagger.json

    
    longitude = fields.Float(required=False)
    
    latitude = fields.Float(required=False)
    

