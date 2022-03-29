"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .StoreDetail import StoreDetail





from .Seller import Seller

from .CompanyDetail import CompanyDetail





from .ProductStockPrice import ProductStockPrice




class ProductStockStatusItem(BaseSchema):
    # Catalog swagger.json

    
    store = fields.Nested(StoreDetail, required=False)
    
    quantity = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    company = fields.Nested(CompanyDetail, required=False)
    
    item_id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    identifier = fields.Dict(required=False)
    

