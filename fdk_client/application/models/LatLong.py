"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class LatLong(BaseSchema):
    # Catalog swagger.json

    
    coordinates = fields.List(fields.Float(required=False), required=False)
    
    type = fields.Str(required=False)
    

