"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class UserDetail(BaseSchema):
    # Catalog swagger.json

    
    username = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    super_user = fields.Boolean(required=False)
    
    user_id = fields.Str(required=False)
    

