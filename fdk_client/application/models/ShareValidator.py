"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class ShareValidator:
    
    class getApplicationQRCode(BaseSchema):
        
        pass 
    
    class getProductQRCodeBySlug(BaseSchema):
        
        slug = fields.Str(required=False)
         
    
    class getCollectionQRCodeBySlug(BaseSchema):
        
        slug = fields.Str(required=False)
         
    
    class getUrlQRCode(BaseSchema):
        
        url = fields.Str(required=False)
         
    
    class createShortLink(BaseSchema):
        
        pass 
    
    class getShortLinkByHash(BaseSchema):
        
        hash = fields.Str(required=False)
         
    
    class getOriginalShortLinkByHash(BaseSchema):
        
        hash = fields.Str(required=False)
         
    