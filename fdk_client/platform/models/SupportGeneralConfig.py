"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CommunicationDetails import CommunicationDetails

from .CommunicationDetails import CommunicationDetails

from .CommunicationDetails import CommunicationDetails








class SupportGeneralConfig(BaseSchema):
    # Lead swagger.json

    
    _id = fields.Str(required=False)
    
    support_email = fields.Nested(CommunicationDetails, required=False)
    
    support_phone = fields.Nested(CommunicationDetails, required=False)
    
    support_faq = fields.Nested(CommunicationDetails, required=False)
    
    show_communication_info = fields.Boolean(required=False)
    
    show_support_dris = fields.Boolean(required=False)
    
    integration = fields.Dict(required=False)
    

