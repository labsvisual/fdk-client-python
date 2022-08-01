"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ErrorResponse(BaseSchema):
    # Catalog swagger.json

    
    code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    

