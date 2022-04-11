"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class GTIN(BaseSchema):
    # Catalog swagger.json

    
    primary = fields.Boolean(required=False)
    
    gtin_type = fields.Str(required=False)
    
    gtin_value = fields.Str(required=False)
    

