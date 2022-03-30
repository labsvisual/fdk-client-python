"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class InventoryValidator:
    
    class getJobsByCompany(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class updateJob(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class createJob(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getJobSteps(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        job_id = fields.Int(required=False)
         
    
    class getJobByCompanyAndIntegration(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        integration_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class disable(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        integration_id = fields.Str(required=False)
         
    
    class getJobConfigDefaults(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getJobByCode(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        code = fields.Str(required=False)
         
    
    class getJobCodeMetrics(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        code = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        status = fields.Str(required=False)
        
        date = fields.Str(required=False)
         
    
    class getJobCodesByCompanyAndIntegration(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        integration_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getJobConfigByIntegrationType(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        integration_type = fields.Str(required=False)
        
        disable = fields.Boolean(required=False)
         
    
    class getJobCodesMetrics(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        daily_job = fields.Boolean(required=False)
        
        job_code = fields.Str(required=False)
         
    
    class saveJobCodesMetrics(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    