"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class ThemeValidator:
    
    class getAllPages(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class createPage(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class updateMultiplePages(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class getPage(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        page_value = fields.Str(required=False)
         
    
    class updatePage(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        page_value = fields.Str(required=False)
         
    
    class deletePage(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        page_value = fields.Str(required=False)
         
    
    class getThemeLibrary(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
         
    
    class addToThemeLibrary(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class applyTheme(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class isUpgradable(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class upgradeTheme(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class getPublicThemes(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
         
    
    class createTheme(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAppliedTheme(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getFonts(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getThemeById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class updateTheme(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class deleteTheme(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class getThemeForPreview(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class publishTheme(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class unpublishTheme(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class archiveTheme(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class unarchiveTheme(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class getThemeLastModified(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    