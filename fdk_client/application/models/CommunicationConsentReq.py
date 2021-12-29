"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class CommunicationConsentReq(BaseSchema):
    # Communication swagger.json

    
    response = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    channel = fields.Str(required=False)
    

