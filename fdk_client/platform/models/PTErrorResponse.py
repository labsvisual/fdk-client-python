"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class PTErrorResponse(BaseSchema):
    # Catalog swagger.json

    
    code = fields.Str(required=False)
    
    errors = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    status = fields.Int(required=False)
    

