"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .InventoryBrand import InventoryBrand

from .InventoryStore import InventoryStore

from .InventoryCategory import InventoryCategory

from .InventoryPrice import InventoryPrice

from .InventoryDiscount import InventoryDiscount














class AppInventoryConfig(BaseSchema):
    # Configuration swagger.json

    
    brand = fields.Nested(InventoryBrand, required=False)
    
    store = fields.Nested(InventoryStore, required=False)
    
    category = fields.Nested(InventoryCategory, required=False)
    
    price = fields.Nested(InventoryPrice, required=False)
    
    discount = fields.Nested(InventoryDiscount, required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
    only_verified_products = fields.Boolean(required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    exclude_category = fields.List(fields.Raw(required=False), required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    company_store = fields.List(fields.Raw(required=False), required=False)
    

