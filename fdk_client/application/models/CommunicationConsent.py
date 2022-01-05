"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CommunicationConsentChannels import CommunicationConsentChannels


class CommunicationConsent(BaseSchema):
    # Communication swagger.json

    
    app_id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    channels = fields.Nested(CommunicationConsentChannels, required=False)
    

