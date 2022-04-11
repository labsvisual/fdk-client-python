"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class CatalogValidator:
    
    class getSearchKeywords(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class deleteSearchKeywords(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateSearchKeywords(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class createCustomKeyword(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAllSearchKeyword(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAutocompleteKeywordDetail(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class deleteAutocompleteKeyword(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateAutocompleteKeyword(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class createCustomAutocompleteRule(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAutocompleteConfig(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class createProductBundle(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class getProductBundle(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        slug = fields.List(fields.Str(required=False), required=False)
         
    
    class getProductBundleDetail(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateProductBundle(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class createSizeGuide(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class getSizeGuides(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        active = fields.Boolean(required=False)
        
        q = fields.Str(required=False)
        
        tag = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getSizeGuide(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateSizeGuide(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateAppProduct(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        item_id = fields.Str(required=False)
         
    
    class getCatalogConfiguration(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class createConfigurationProductListing(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getConfigurations(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class createConfigurationByType(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        type = fields.Str(required=False)
         
    
    class getConfigurationByType(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        type = fields.Str(required=False)
         
    
    class getQueryFilters(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class createCollection(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAllCollections(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        tags = fields.List(fields.Str(required=False), required=False)
        
        is_active = fields.Boolean(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getCollectionDetail(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
    
    class deleteCollection(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateCollection(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class addCollectionItems(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getCollectionItems(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        sort_on = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getCatalogInsights(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        brand = fields.Str(required=False)
         
    
    class getSellerInsights(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        seller_app_id = fields.Str(required=False)
         
    
    class createMarketplaceOptin(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        marketplace = fields.Str(required=False)
         
    
    class getMarketplaceOptinDetail(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getCompanyDetail(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getCompanyBrandDetail(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        is_active = fields.Boolean(required=False)
        
        q = fields.Boolean(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        marketplace = fields.Str(required=False)
         
    
    class getCompanyMetrics(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getStoreDetail(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getGenderAttribute(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        attribute_slug = fields.Str(required=False)
         
    
    class listProductTemplateCategories(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        departments = fields.Str(required=False)
        
        item_type = fields.Str(required=False)
         
    
    class listDepartmentsData(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        name = fields.Str(required=False)
        
        search = fields.Str(required=False)
        
        is_active = fields.Boolean(required=False)
         
    
    class getDepartmentData(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        uid = fields.Str(required=False)
         
    
    class listProductTemplate(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        department = fields.Str(required=False)
         
    
    class validateProductTemplate(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
    
    class downloadProductTemplateViews(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
    
    class downloadProductTemplateView(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        item_type = fields.Str(required=False)
         
    
    class validateProductTemplateSchema(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        item_type = fields.Str(required=False)
         
    
    class listHSNCodes(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class listProductTemplateExportDetails(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class listTemplateBrandTypeValues(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        filter = fields.Str(required=False)
         
    
    class createCategories(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class listCategories(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        level = fields.Str(required=False)
        
        departments = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getCategoryData(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        uid = fields.Str(required=False)
         
    
    class updateCategory(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        uid = fields.Str(required=False)
         
    
    class createProduct(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class getProducts(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        brand_ids = fields.List(fields.Int(required=False), required=False)
        
        category_ids = fields.List(fields.Int(required=False), required=False)
        
        item_ids = fields.List(fields.Int(required=False), required=False)
        
        department_ids = fields.List(fields.Int(required=False), required=False)
        
        item_code = fields.List(fields.Str(required=False), required=False)
        
        q = fields.Str(required=False)
        
        tags = fields.List(fields.Str(required=False), required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getProduct(BaseSchema):
        
        item_code = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        item_id = fields.Int(required=False)
        
        brand_uid = fields.Int(required=False)
         
    
    class deleteProduct(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        item_id = fields.Int(required=False)
         
    
    class editProduct(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        item_id = fields.Int(required=False)
         
    
    class getProductValidation(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getProductSize(BaseSchema):
        
        item_code = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        item_id = fields.Int(required=False)
        
        brand_uid = fields.Int(required=False)
        
        uid = fields.Int(required=False)
         
    
    class updateProductAssetsInBulk(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getProductBulkUploadHistory(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class createProductsInBulk(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        batch_id = fields.Str(required=False)
         
    
    class deleteProductBulkJob(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        batch_id = fields.Int(required=False)
         
    
    class getProductTags(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class createProductAssetsInBulk(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getProductAssetsInBulk(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class deleteSize(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        item_id = fields.Int(required=False)
        
        size = fields.Int(required=False)
         
    
    class addInventory(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        item_id = fields.Float(required=False)
        
        size = fields.Str(required=False)
         
    
    class getInventoryBySize(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        item_id = fields.Str(required=False)
        
        size = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        sellable = fields.Boolean(required=False)
         
    
    class getInventoryBySizeIdentifier(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        item_id = fields.Str(required=False)
        
        size_identifier = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        location_ids = fields.List(fields.Int(required=False), required=False)
         
    
    class getDiscountedInventoryBySizeIdentifier(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        item_id = fields.Int(required=False)
        
        size_identifier = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        location_ids = fields.List(fields.Int(required=False), required=False)
         
    
    class deleteInventory(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        size = fields.Str(required=False)
        
        item_id = fields.Int(required=False)
        
        location_id = fields.Float(required=False)
         
    
    class createBulkInventoryJob(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getInventoryBulkUploadHistory(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class createBulkInventory(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        batch_id = fields.Str(required=False)
         
    
    class deleteBulkInventoryJob(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
         
    
    class createInventoryExportJob(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getInventoryExport(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class exportInventoryConfig(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        filter_type = fields.Str(required=False)
         
    
    class createHsnCode(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class getAllHsnCodes(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
    
    class getHsnCode(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateHsnCode(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class bulkHsnCode(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class getApplicationBrands(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        department = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        brand_id = fields.List(fields.Int(required=False), required=False)
         
    
    class getDepartments(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getCategories(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        department = fields.Str(required=False)
         
    
    class getAppicationProducts(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        f = fields.Str(required=False)
        
        filters = fields.Boolean(required=False)
        
        sort_on = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_type = fields.Str(required=False)
        
        item_ids = fields.List(fields.Int(required=False), required=False)
         
    
    class getProductDetailBySlug(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
    
    class getAppProducts(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        brand_ids = fields.List(fields.Int(required=False), required=False)
        
        category_ids = fields.List(fields.Int(required=False), required=False)
        
        department_ids = fields.List(fields.Int(required=False), required=False)
        
        tags = fields.List(fields.Str(required=False), required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
    
    class getOptimalLocations(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class getAppLocations(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        store_type = fields.Str(required=False)
        
        uid = fields.List(fields.Int(required=False), required=False)
        
        q = fields.Str(required=False)
        
        stage = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    