"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class DepartmentErrorResponse(BaseSchema):
    # Catalog swagger.json

    
    errors = fields.Dict(required=False)
    
    code = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    status = fields.Int(required=False)
    

