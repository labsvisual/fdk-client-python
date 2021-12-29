"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class CommonResponse(BaseSchema):
    # Catalog swagger.json

    
    success = fields.Str(required=False)
    

