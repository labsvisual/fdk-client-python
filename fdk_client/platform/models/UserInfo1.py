"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class UserInfo1(BaseSchema):
    # Catalog swagger.json

    
    email = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    

