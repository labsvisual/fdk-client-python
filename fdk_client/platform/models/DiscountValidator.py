"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class DiscountValidator:
    
    class getDiscounts(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        view = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        archived = fields.Boolean(required=False)
        
        month = fields.Int(required=False)
        
        year = fields.Int(required=False)
        
        type = fields.Str(required=False)
        
        app_ids = fields.List(fields.Str(required=False), required=False)
         
    
    class createDiscount(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getDiscount(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateDiscount(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
         
    
    class validateDiscountFile(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        discount = fields.Str(required=False)
         
    
    class downloadDiscountFile(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        type = fields.Str(required=False)
         
    
    class getValidationJob(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
         
    
    class cancelValidationJob(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
         
    
    class getDownloadJob(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
         
    
    class cancelDownloadJob(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
         
    