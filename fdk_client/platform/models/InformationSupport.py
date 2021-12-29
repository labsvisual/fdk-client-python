"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class InformationSupport(BaseSchema):
    # Configuration swagger.json

    
    phone = fields.List(fields.Str(required=False), required=False)
    
    email = fields.List(fields.Str(required=False), required=False)
    
    timing = fields.Str(required=False)
    

