"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class FeedbackValidator:
    
    class getAttributes(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getCustomerReviews(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        entity_id = fields.Str(required=False)
        
        entity_type = fields.Str(required=False)
        
        user_id = fields.Str(required=False)
        
        media = fields.Str(required=False)
        
        rating = fields.List(fields.Float(required=False), required=False)
        
        attribute_rating = fields.List(fields.Str(required=False), required=False)
        
        facets = fields.Boolean(required=False)
        
        sort = fields.Str(required=False)
        
        next = fields.Str(required=False)
        
        start = fields.Str(required=False)
        
        limit = fields.Str(required=False)
        
        count = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class updateApprove(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        review_id = fields.Str(required=False)
         
    
    class getHistory(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        review_id = fields.Str(required=False)
         
    
    class getApplicationTemplates(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class createTemplate(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getTemplateById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateTemplate(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateTemplateStatus(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    