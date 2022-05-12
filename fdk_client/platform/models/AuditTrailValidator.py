"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class AuditTrailValidator:
    
    class getAuditLogs(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        qs = fields.Str(required=False)
         
    
    class createAuditLog(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class getAuditLog(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getEntityTypes(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    