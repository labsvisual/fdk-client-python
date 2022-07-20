"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ManufacturerResponse(BaseSchema):
    # Catalog swagger.json

    
    address = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    

