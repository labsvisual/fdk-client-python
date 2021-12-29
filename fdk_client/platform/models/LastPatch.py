"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class LastPatch(BaseSchema):
    # Configuration swagger.json

    
    op = fields.Str(required=False)
    
    path = fields.Str(required=False)
    
    value = fields.Str(required=False)
    

