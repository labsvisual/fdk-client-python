"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class InventoryValidationResponse(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    

