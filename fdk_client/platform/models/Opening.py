"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Opening(BaseSchema):
    # Order swagger.json

    
    minute = fields.Int(required=False)
    
    hour = fields.Int(required=False)
    

