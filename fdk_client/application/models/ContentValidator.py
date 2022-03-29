"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class ContentValidator:
    
    class getAnnouncements(BaseSchema):
        
        pass 
    
    class getBlog(BaseSchema):
        
        slug = fields.Str(required=False)
        
        root_id = fields.Str(required=False)
         
    
    class getBlogs(BaseSchema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getDataLoaders(BaseSchema):
        
        pass 
    
    class getFaqs(BaseSchema):
        
        pass 
    
    class getFaqCategories(BaseSchema):
        
        pass 
    
    class getFaqBySlug(BaseSchema):
        
        slug = fields.Str(required=False)
         
    
    class getFaqCategoryBySlug(BaseSchema):
        
        slug = fields.Str(required=False)
         
    
    class getFaqsByCategorySlug(BaseSchema):
        
        slug = fields.Str(required=False)
         
    
    class getLandingPage(BaseSchema):
        
        pass 
    
    class getLegalInformation(BaseSchema):
        
        pass 
    
    class getNavigations(BaseSchema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getSEOConfiguration(BaseSchema):
        
        pass 
    
    class getSlideshows(BaseSchema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getSlideshow(BaseSchema):
        
        slug = fields.Str(required=False)
         
    
    class getSupportInformation(BaseSchema):
        
        pass 
    
    class getTags(BaseSchema):
        
        pass 
    
    class getPage(BaseSchema):
        
        slug = fields.Str(required=False)
        
        root_id = fields.Str(required=False)
         
    
    class getPages(BaseSchema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    