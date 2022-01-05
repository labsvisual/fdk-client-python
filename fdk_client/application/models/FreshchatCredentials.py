"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class FreshchatCredentials(BaseSchema):
    # Configuration swagger.json

    
    app_id = fields.Str(required=False)
    
    app_key = fields.Str(required=False)
    
    web_token = fields.Str(required=False)
    

