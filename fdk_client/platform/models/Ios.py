"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Ios(BaseSchema):
    # Configuration swagger.json

    
    application_id = fields.Str(required=False)
    
    api_key = fields.Str(required=False)
    

