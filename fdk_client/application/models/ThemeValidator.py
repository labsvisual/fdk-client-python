"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class ThemeValidator:
    
    class getAllPages(BaseSchema):
        
        theme_id = fields.Str(required=False)
         
    
    class getPage(BaseSchema):
        
        theme_id = fields.Str(required=False)
        
        page_value = fields.Str(required=False)
         
    
    class getAppliedTheme(BaseSchema):
        
        pass 
    
    class getThemeForPreview(BaseSchema):
        
        theme_id = fields.Str(required=False)
         
    