"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class ConfigurationValidator:
    
    class getApplication(BaseSchema):
        
        pass 
    
    class getOwnerInfo(BaseSchema):
        
        pass 
    
    class getBasicDetails(BaseSchema):
        
        pass 
    
    class getIntegrationTokens(BaseSchema):
        
        pass 
    
    class getOrderingStores(BaseSchema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
    
    class getStoreDetailById(BaseSchema):
        
        store_id = fields.Int(required=False)
         
    
    class getFeatures(BaseSchema):
        
        pass 
    
    class getContactInfo(BaseSchema):
        
        pass 
    
    class getCurrencies(BaseSchema):
        
        pass 
    
    class getCurrencyById(BaseSchema):
        
        id = fields.Str(required=False)
         
    
    class getAppCurrencies(BaseSchema):
        
        pass 
    
    class getLanguages(BaseSchema):
        
        pass 
    
    class getOrderingStoreCookie(BaseSchema):
        
        pass 
    
    class removeOrderingStoreCookie(BaseSchema):
        
        pass 
    
    class getAppStaffList(BaseSchema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        order_incent = fields.Boolean(required=False)
        
        ordering_store = fields.Int(required=False)
        
        user = fields.Str(required=False)
         
    
    class getAppStaffs(BaseSchema):
        
        order_incent = fields.Boolean(required=False)
        
        ordering_store = fields.Int(required=False)
        
        user = fields.Str(required=False)
         
    