"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class WeightResponse(BaseSchema):
    # Catalog swagger.json

    
    unit = fields.Str(required=False)
    
    shipping = fields.Float(required=False)
    
    is_default = fields.Boolean(required=False)
    

