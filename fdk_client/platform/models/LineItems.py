"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .LineItemsArticle import LineItemsArticle





























from .PriceSet import PriceSet

from .TaxLines import TaxLines





from .TotalDiscountSet import TotalDiscountSet


class LineItems(BaseSchema):
    # Order swagger.json

    
    sku = fields.Str(required=False)
    
    fulfillable_quantity = fields.Int(required=False)
    
    grams = fields.Int(required=False)
    
    total_discount = fields.Str(required=False)
    
    article = fields.Nested(LineItemsArticle, required=False)
    
    title = fields.Str(required=False)
    
    variant_inventory_management = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    variant_id = fields.Int(required=False)
    
    variant_title = fields.Str(required=False)
    
    product_exists = fields.Boolean(required=False)
    
    price = fields.Str(required=False)
    
    admin_graphql_api_id = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    vendor = fields.Str(required=False)
    
    fulfillment_service = fields.Str(required=False)
    
    taxable = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    product_id = fields.Int(required=False)
    
    price_set = fields.Nested(PriceSet, required=False)
    
    tax_lines = fields.Nested(TaxLines, required=False)
    
    requires_shipping = fields.Boolean(required=False)
    
    gift_card = fields.Boolean(required=False)
    
    total_discount_set = fields.Nested(TotalDiscountSet, required=False)
    

