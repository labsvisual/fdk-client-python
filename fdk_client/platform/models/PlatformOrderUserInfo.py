"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class PlatformOrderUserInfo(BaseSchema):
    # Order swagger.json

    
    mobile = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    is_anonymous_user = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
    avis_user_id = fields.Str(required=False)
    

