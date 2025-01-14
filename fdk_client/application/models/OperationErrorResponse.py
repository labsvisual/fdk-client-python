"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class OperationErrorResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    

