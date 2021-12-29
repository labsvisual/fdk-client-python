"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class WebhookValidator:
    
    class getSubscribersByCompany(BaseSchema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        company_id = fields.Int(required=False)
        
        extension_id = fields.Str(required=False)
         
    
    class registerSubscriberToEvent(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class updateSubscriberConfig(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getSubscribersByExtensionId(BaseSchema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        company_id = fields.Int(required=False)
        
        extension_id = fields.Str(required=False)
         
    
    class getSubscriberById(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        subscriber_id = fields.Int(required=False)
         
    
    class fetchAllEventConfigurations(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    