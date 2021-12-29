"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PlatformOrderDetailsPage(BaseSchema):
    # Order swagger.json

    
    next = fields.Str(required=False)
    
    previous = fields.Str(required=False)
    

