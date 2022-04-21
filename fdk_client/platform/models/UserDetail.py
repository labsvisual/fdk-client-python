"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class UserDetail(BaseSchema):
    # Catalog swagger.json

    
    username = fields.Str(required=False)
    
    full_name = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    

