"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class UserCommon(BaseSchema):
    # Catalog swagger.json

    
    username = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    user_id = fields.Str(required=False)
    

