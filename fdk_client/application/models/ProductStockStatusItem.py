"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductStockPrice import ProductStockPrice





from .CompanyDetail import CompanyDetail



from .StoreDetail import StoreDetail

from .Seller import Seller




class ProductStockStatusItem(BaseSchema):
    # Catalog swagger.json

    
    identifier = fields.Dict(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    quantity = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    
    company = fields.Nested(CompanyDetail, required=False)
    
    size = fields.Str(required=False)
    
    store = fields.Nested(StoreDetail, required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    uid = fields.Str(required=False)
    

