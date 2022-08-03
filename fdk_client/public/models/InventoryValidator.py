"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class InventoryValidator:
    
    class getConfigByApiKey(BaseSchema):
        
        apikey = fields.Str(required=False)
         
    
    class getApiKey(BaseSchema):
        
        user_name = fields.Str(required=False)
        
        password = fields.Str(required=False)
         
    
    class getJobByCode(BaseSchema):
        
        code = fields.Str(required=False)
         
    
    class getJobConfigByIntegrationType(BaseSchema):
        
        integration_type = fields.Str(required=False)
        
        disable = fields.Boolean(required=False)
         
    
    class getJobCodesMetrics(BaseSchema):
        
        daily_job = fields.Boolean(required=False)
        
        job_code = fields.Str(required=False)
         
    
    class saveJobCodesMetrics(BaseSchema):
        
        pass 
    