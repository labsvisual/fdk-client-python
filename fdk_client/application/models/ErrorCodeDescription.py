"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ErrorCodeDescription(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    

