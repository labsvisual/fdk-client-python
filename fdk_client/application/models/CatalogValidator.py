"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class CatalogValidator:
    
    class getProductDetailBySlug(BaseSchema):
        
        slug = fields.Str(required=False)
         
    
    class getProductSizesBySlug(BaseSchema):
        
        slug = fields.Str(required=False)
        
        store_id = fields.Int(required=False)
         
    
    class getProductComparisonBySlugs(BaseSchema):
        
        slug = fields.List(fields.Str(required=False), required=False)
         
    
    class getSimilarComparisonProductBySlug(BaseSchema):
        
        slug = fields.Str(required=False)
         
    
    class getComparedFrequentlyProductBySlug(BaseSchema):
        
        slug = fields.Str(required=False)
         
    
    class getProductSimilarByIdentifier(BaseSchema):
        
        slug = fields.Str(required=False)
        
        similar_type = fields.Str(required=False)
         
    
    class getProductVariantsBySlug(BaseSchema):
        
        slug = fields.Str(required=False)
         
    
    class getProductStockByIds(BaseSchema):
        
        item_id = fields.Str(required=False)
        
        alu = fields.Str(required=False)
        
        sku_code = fields.Str(required=False)
        
        ean = fields.Str(required=False)
        
        upc = fields.Str(required=False)
         
    
    class getProductStockForTimeByIds(BaseSchema):
        
        timestamp = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_id = fields.Str(required=False)
         
    
    class getProducts(BaseSchema):
        
        q = fields.Str(required=False)
        
        f = fields.Str(required=False)
        
        filters = fields.Boolean(required=False)
        
        sort_on = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_type = fields.Str(required=False)
         
    
    class getBrands(BaseSchema):
        
        department = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getBrandDetailBySlug(BaseSchema):
        
        slug = fields.Str(required=False)
         
    
    class getCategories(BaseSchema):
        
        department = fields.Str(required=False)
         
    
    class getCategoryDetailBySlug(BaseSchema):
        
        slug = fields.Str(required=False)
         
    
    class getHomeProducts(BaseSchema):
        
        sort_on = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getDepartments(BaseSchema):
        
        pass 
    
    class getSearchResults(BaseSchema):
        
        q = fields.Str(required=False)
         
    
    class getCollections(BaseSchema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        tag = fields.List(fields.Str(required=False), required=False)
         
    
    class getCollectionItemsBySlug(BaseSchema):
        
        slug = fields.Str(required=False)
        
        f = fields.Str(required=False)
        
        filters = fields.Boolean(required=False)
        
        sort_on = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getCollectionDetailBySlug(BaseSchema):
        
        slug = fields.Str(required=False)
         
    
    class getFollowedListing(BaseSchema):
        
        collection_type = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class unfollowById(BaseSchema):
        
        collection_type = fields.Str(required=False)
        
        collection_id = fields.Str(required=False)
         
    
    class followById(BaseSchema):
        
        collection_type = fields.Str(required=False)
        
        collection_id = fields.Str(required=False)
         
    
    class getFollowerCountById(BaseSchema):
        
        collection_type = fields.Str(required=False)
        
        collection_id = fields.Str(required=False)
         
    
    class getFollowIds(BaseSchema):
        
        collection_type = fields.Str(required=False)
         
    
    class getStores(BaseSchema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        city = fields.Str(required=False)
        
        range = fields.Int(required=False)
        
        latitude = fields.Float(required=False)
        
        longitude = fields.Float(required=False)
         
    
    class getInStockLocations(BaseSchema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        city = fields.Str(required=False)
        
        range = fields.Int(required=False)
        
        latitude = fields.Float(required=False)
        
        longitude = fields.Float(required=False)
         
    
    class getLocationDetailsById(BaseSchema):
        
        location_id = fields.Int(required=False)
         
    
    class getProductBundlesBySlug(BaseSchema):
        
        slug = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getProductPriceBySlug(BaseSchema):
        
        slug = fields.Str(required=False)
        
        size = fields.Str(required=False)
        
        store_id = fields.Int(required=False)
        
        pincode = fields.Str(required=False)
         
    
    class getProductSellersBySlug(BaseSchema):
        
        slug = fields.Str(required=False)
        
        size = fields.Str(required=False)
        
        pincode = fields.Str(required=False)
        
        strategy = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    