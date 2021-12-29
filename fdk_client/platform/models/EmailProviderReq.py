"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .EmailProviderReqFrom import EmailProviderReqFrom


class EmailProviderReq(BaseSchema):
    # Communication swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    api_key = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
    from_ = fields.List(fields.Nested(EmailProviderReqFrom, required=False), required=False)
    

