"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .StoreDetail import StoreDetail

from .Seller import Seller

from .ProductStockPrice import ProductStockPrice

from .CompanyDetail import CompanyDetail




class ProductStockStatusItem(BaseSchema):
    # Catalog swagger.json

    
    item_id = fields.Int(required=False)
    
    identifier = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    store = fields.Nested(StoreDetail, required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    company = fields.Nested(CompanyDetail, required=False)
    
    quantity = fields.Int(required=False)
    

