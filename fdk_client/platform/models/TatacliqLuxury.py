"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class TatacliqLuxury(BaseSchema):
    # Order swagger.json

    
    sku = fields.Str(required=False)
    

