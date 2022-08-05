"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class UsesRemaining1(BaseSchema):
    # Cart swagger.json

    
    total = fields.Int(required=False)
    
    user = fields.Int(required=False)
    

