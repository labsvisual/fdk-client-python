"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .EmailProviderReqFrom import EmailProviderReqFrom




















class EmailProvider(BaseSchema):
    # Communication swagger.json

    
    type = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
    from_address = fields.List(fields.Nested(EmailProviderReqFrom, required=False), required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    api_key = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    

