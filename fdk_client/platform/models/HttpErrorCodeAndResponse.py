"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ErrorCodeAndDescription import ErrorCodeAndDescription




class HttpErrorCodeAndResponse(BaseSchema):
    # Payment swagger.json

    
    error = fields.Nested(ErrorCodeAndDescription, required=False)
    
    success = fields.Boolean(required=False)
    

