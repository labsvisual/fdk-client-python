"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class AnalyticsValidator:
    
    class getStatiscticsGroups(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getStatiscticsGroupComponents(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        group_name = fields.Str(required=False)
         
    
    class getComponentStatsCSV(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        component_name = fields.Str(required=False)
         
    
    class getComponentStatsPDF(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        component_name = fields.Str(required=False)
         
    
    class getComponentStats(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        component_name = fields.Str(required=False)
         
    
    class getAbandonCartList(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getAbandonCartsCSV(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
         
    
    class getAbandonCartDetail(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        cart_id = fields.Str(required=False)
         
    
    class createExportJob(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        export_type = fields.Str(required=False)
         
    
    class getExportJobStatus(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        export_type = fields.Str(required=False)
        
        job_id = fields.Str(required=False)
         
    
    class getLogsList(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        log_type = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class searchLogs(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        log_type = fields.Str(required=False)
         
    