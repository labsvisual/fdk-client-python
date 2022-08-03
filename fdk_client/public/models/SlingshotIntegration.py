"""Public Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .Metum import Metum


class SlingshotIntegration(BaseSchema):
    # Inventory swagger.json

    
    _id = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    meta = fields.List(fields.Nested(Metum, required=False), required=False)
    

