"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class IfscCodeResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    branch_name = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    

