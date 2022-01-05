"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class UserDetails(BaseSchema):
    # Discount swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    

