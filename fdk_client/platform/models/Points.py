"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class Points(BaseSchema):
    # Rewards swagger.json

    
    available = fields.Float(required=False)
    

