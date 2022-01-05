"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class CommunicationValidator:
    
    class getCommunicationConsent(BaseSchema):
        
        pass 
    
    class upsertCommunicationConsent(BaseSchema):
        
        pass 
    
    class upsertAppPushtoken(BaseSchema):
        
        pass 
    