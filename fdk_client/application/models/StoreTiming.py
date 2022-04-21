"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Time import Time





from .Time import Time


class StoreTiming(BaseSchema):
    # Catalog swagger.json

    
    opening = fields.Nested(Time, required=False)
    
    weekday = fields.Str(required=False)
    
    open = fields.Boolean(required=False)
    
    closing = fields.Nested(Time, required=False)
    

