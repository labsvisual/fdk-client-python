"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class FileStorageValidator:
    
    class startUpload(BaseSchema):
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
    
    class completeUpload(BaseSchema):
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
    
    class appStartUpload(BaseSchema):
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class appCompleteUpload(BaseSchema):
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getSignUrls(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class copyFiles(BaseSchema):
        
        sync = fields.Boolean(required=False)
        
        company_id = fields.Int(required=False)
         
    
    class appCopyFiles(BaseSchema):
        
        sync = fields.Boolean(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Int(required=False)
         
    
    class browse(BaseSchema):
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
         
    
    class browse(BaseSchema):
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
         
    
    class proxy(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        url = fields.Str(required=False)
         
    