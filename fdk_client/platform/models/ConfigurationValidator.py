"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class ConfigurationValidator:
    
    class getBuildConfig(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        platform_type = fields.Str(required=False)
         
    
    class updateBuildConfig(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        platform_type = fields.Str(required=False)
         
    
    class getPreviousVersions(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        platform_type = fields.Str(required=False)
         
    
    class getAppFeatures(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updateAppFeatures(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAppBasicDetails(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updateAppBasicDetails(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAppContactInfo(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updateAppContactInfo(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAppApiTokens(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updateAppApiTokens(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAppCompanies(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        uid = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getAppStores(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getInventoryConfig(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updateInventoryConfig(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class partiallyUpdateInventoryConfig(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAppCurrencyConfig(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updateAppCurrencyConfig(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAppSupportedCurrency(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getOrderingStoresByFilter(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class updateOrderingStoreConfig(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getStaffOrderingStores(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
    
    class getDomains(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class addDomain(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class removeDomainById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class changeDomainType(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getDomainStatus(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class createApplication(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class getApplications(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
    
    class getApplicationById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getCurrencies(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class getDomainAvailibility(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class getIntegrationById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Int(required=False)
         
    
    class getAvailableOptIns(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getSelectedOptIns(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        level = fields.Str(required=False)
        
        uid = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getIntegrationLevelConfig(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        level = fields.Str(required=False)
        
        opted = fields.Boolean(required=False)
        
        check_permission = fields.Boolean(required=False)
         
    
    class updateLevelIntegration(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        level = fields.Str(required=False)
         
    
    class getIntegrationByLevelId(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        level = fields.Str(required=False)
        
        uid = fields.Int(required=False)
         
    
    class updateLevelUidIntegration(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        level = fields.Str(required=False)
        
        uid = fields.Int(required=False)
         
    
    class getLevelActiveIntegrations(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        level = fields.Str(required=False)
        
        uid = fields.Int(required=False)
         
    
    class getBrandsByCompany(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        q = fields.Str(required=False)
         
    
    class getCompanyByBrands(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getStoreByBrands(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getOtherSellerApplications(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getOtherSellerApplicationById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class optOutFromApplication(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    