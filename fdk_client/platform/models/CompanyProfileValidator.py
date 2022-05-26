"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class CompanyProfileValidator:
    
    class cbsOnboardGet(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class updateCompany(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class getCompanyMetrics(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class editBrand(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        brand_id = fields.Str(required=False)
         
    
    class getBrand(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        brand_id = fields.Str(required=False)
         
    
    class createBrand(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class createCompanyBrandMapping(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class getBrands(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
    
    class createLocation(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class getLocations(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        store_type = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        stage = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class updateLocation(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        location_id = fields.Str(required=False)
         
    
    class getLocationDetail(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        location_id = fields.Str(required=False)
         
    
    class createLocationBulk(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    