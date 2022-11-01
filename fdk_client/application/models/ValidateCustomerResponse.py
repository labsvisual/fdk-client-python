"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ValidateCustomerResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    

