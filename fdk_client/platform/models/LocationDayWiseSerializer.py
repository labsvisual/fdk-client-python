"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .LocationTimingSerializer import LocationTimingSerializer

from .LocationTimingSerializer import LocationTimingSerializer


class LocationDayWiseSerializer(BaseSchema):
    # Catalog swagger.json

    
    weekday = fields.Str(required=False)
    
    open = fields.Boolean(required=False)
    
    opening = fields.Nested(LocationTimingSerializer, required=False)
    
    closing = fields.Nested(LocationTimingSerializer, required=False)
    

