"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class SafetynetCredentials(BaseSchema):
    # Configuration swagger.json

    
    api_key = fields.Str(required=False)
    

