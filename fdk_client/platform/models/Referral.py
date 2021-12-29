"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class Referral(BaseSchema):
    # Rewards swagger.json

    
    code = fields.Str(required=False)
    

