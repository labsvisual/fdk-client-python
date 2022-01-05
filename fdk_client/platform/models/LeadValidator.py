"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class LeadValidator:
    
    class getTickets(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        items = fields.Boolean(required=False)
        
        filters = fields.Boolean(required=False)
        
        q = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        priority = fields.Str(required=False, validate=OneOf([val.value for val in PriorityEnum.__members__.values()]))
        
        category = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class createTicket(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class getTickets(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        items = fields.Boolean(required=False)
        
        filters = fields.Boolean(required=False)
        
        q = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        priority = fields.Str(required=False, validate=OneOf([val.value for val in PriorityEnum.__members__.values()]))
        
        category = fields.Str(required=False)
         
    
    class getTicket(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class editTicket(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getTicket(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class editTicket(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class createHistory(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getTicketHistory(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getFeedbacks(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class submitFeedback(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class createHistory(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getTicketHistory(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getCustomForm(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
    
    class editCustomForm(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
    
    class getCustomForms(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class createCustomForm(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getTokenForVideoRoom(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        unique_name = fields.Str(required=False)
         
    
    class getTokenForVideoRoom(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        unique_name = fields.Str(required=False)
         
    
    class getVideoParticipants(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        unique_name = fields.Str(required=False)
         
    
    class getVideoParticipants(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        unique_name = fields.Str(required=False)
         
    
    class openVideoRoom(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class closeVideoRoom(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        unique_name = fields.Str(required=False)
         
    