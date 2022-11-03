"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class DimensionResponse(BaseSchema):
    # Catalog swagger.json

    
    height = fields.Float(required=False)
    
    is_default = fields.Boolean(required=False)
    
    unit = fields.Str(required=False)
    
    width = fields.Float(required=False)
    
    length = fields.Float(required=False)
    

