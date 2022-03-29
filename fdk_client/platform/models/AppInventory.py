"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .InventoryBrandRule import InventoryBrandRule

from .InventoryStoreRule import InventoryStoreRule









from .InventoryPaymentConfig import InventoryPaymentConfig

from .InventoryArticleAssignment import InventoryArticleAssignment


class AppInventory(BaseSchema):
    # Configuration swagger.json

    
    brand = fields.Nested(InventoryBrandRule, required=False)
    
    store = fields.Nested(InventoryStoreRule, required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
    only_verified_products = fields.Boolean(required=False)
    
    payment = fields.Nested(InventoryPaymentConfig, required=False)
    
    article_assignment = fields.Nested(InventoryArticleAssignment, required=False)
    

