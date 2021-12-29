"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class CommonValidator:
    
    class getLocations(BaseSchema):
        
        location_type = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    