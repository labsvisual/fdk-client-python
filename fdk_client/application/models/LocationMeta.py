"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Location import Location

from .Location import Location


class LocationMeta(BaseSchema):
    # Feedback swagger.json

    
    demand = fields.Nested(Location, required=False)
    
    supply = fields.Nested(Location, required=False)
    

