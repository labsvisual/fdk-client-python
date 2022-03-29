"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class SaveAddressResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    is_default_address = fields.Boolean(required=False)
    

