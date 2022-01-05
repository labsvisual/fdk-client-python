"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class FyndRewardsCredentials(BaseSchema):
    # Configuration swagger.json

    
    public_key = fields.Str(required=False)
    

