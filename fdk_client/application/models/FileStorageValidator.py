"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class FileStorageValidator:
    
    class startUpload(BaseSchema):
        
        namespace = fields.Str(required=False)
         
    
    class completeUpload(BaseSchema):
        
        namespace = fields.Str(required=False)
         
    
    class signUrls(BaseSchema):
        
        pass 
    