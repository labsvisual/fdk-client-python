"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .MarketPlaceSttributes import MarketPlaceSttributes





from .ProductStockPrice import ProductStockPrice



from .Store import Store

from .StrategyWiseListing import StrategyWiseListing





from .Seller import Seller



from .ProductStockPrice import ProductStockPrice



from .ArticleAssignment import ArticleAssignment

from .ProductSet import ProductSet

from .ReturnConfig import ReturnConfig


class ProductSizePriceResponse(BaseSchema):
    # Catalog swagger.json

    
    long_lat = fields.List(fields.Float(required=False), required=False)
    
    marketplace_attributes = fields.List(fields.Nested(MarketPlaceSttributes, required=False), required=False)
    
    pincode = fields.Int(required=False)
    
    item_type = fields.Str(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    quantity = fields.Int(required=False)
    
    store = fields.Nested(Store, required=False)
    
    strategy_wise_listing = fields.List(fields.Nested(StrategyWiseListing, required=False), required=False)
    
    special_badge = fields.Str(required=False)
    
    article_id = fields.Str(required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    discount = fields.Str(required=False)
    
    price_per_piece = fields.Nested(ProductStockPrice, required=False)
    
    seller_count = fields.Int(required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    set = fields.Nested(ProductSet, required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    

