"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CommunicationConsentChannelsEmail import CommunicationConsentChannelsEmail

from .CommunicationConsentChannelsSms import CommunicationConsentChannelsSms

from .CommunicationConsentChannelsWhatsapp import CommunicationConsentChannelsWhatsapp


class CommunicationConsentChannels(BaseSchema):
    # Communication swagger.json

    
    email = fields.Nested(CommunicationConsentChannelsEmail, required=False)
    
    sms = fields.Nested(CommunicationConsentChannelsSms, required=False)
    
    whatsapp = fields.Nested(CommunicationConsentChannelsWhatsapp, required=False)
    

