"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




















class ShareMessages(BaseSchema):
    # Rewards swagger.json

    
    email = fields.Str(required=False)
    
    facebook = fields.Str(required=False)
    
    fallback = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    messenger = fields.Str(required=False)
    
    sms = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    twitter = fields.Str(required=False)
    
    whatsapp = fields.Str(required=False)
    

