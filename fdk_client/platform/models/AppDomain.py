"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class AppDomain(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    

