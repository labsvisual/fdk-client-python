"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema















from .TotalDiscountsSet import TotalDiscountsSet

from .TotalPriceSet import TotalPriceSet

from .TotalTaxSet import TotalTaxSet





from .SubtotalPriceSet import SubtotalPriceSet































from .LineItems import LineItems







from .BillingAddress import BillingAddress

from .TotalShippingPriceSet import TotalShippingPriceSet

from .Customer import Customer



from .TotalLineItemsPriceSet import TotalLineItemsPriceSet











from .OrderShippingAddress import OrderShippingAddress






class MarketplaceOrder(BaseSchema):
    # Order swagger.json

    
    order_status_url = fields.Str(required=False)
    
    admin_graphql_api_id = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    test = fields.Boolean(required=False)
    
    note = fields.Str(required=False)
    
    total_price = fields.Str(required=False)
    
    app_id = fields.Int(required=False)
    
    total_discounts_set = fields.Nested(TotalDiscountsSet, required=False)
    
    total_price_set = fields.Nested(TotalPriceSet, required=False)
    
    total_tax_set = fields.Nested(TotalTaxSet, required=False)
    
    gateway = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    subtotal_price_set = fields.Nested(SubtotalPriceSet, required=False)
    
    number = fields.Int(required=False)
    
    buyer_accepts_marketing = fields.Boolean(required=False)
    
    contact_email = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    source_name = fields.Str(required=False)
    
    payment_gateway_names = fields.List(fields.Raw(required=False), required=False)
    
    presentment_currency = fields.Str(required=False)
    
    subtotal_price = fields.Str(required=False)
    
    processed_at = fields.Str(required=False)
    
    order_number = fields.Int(required=False)
    
    total_tip_received = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    confirmed = fields.Boolean(required=False)
    
    currency = fields.Str(required=False)
    
    total_line_items_price = fields.Str(required=False)
    
    line_items = fields.Nested(LineItems, required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    total_weight = fields.Int(required=False)
    
    billing_address = fields.Nested(BillingAddress, required=False)
    
    total_shipping_price_set = fields.Nested(TotalShippingPriceSet, required=False)
    
    customer = fields.Nested(Customer, required=False)
    
    total_discounts = fields.Str(required=False)
    
    total_line_items_price_set = fields.Nested(TotalLineItemsPriceSet, required=False)
    
    tags = fields.Str(required=False)
    
    total_price_usd = fields.Str(required=False)
    
    user_id = fields.Int(required=False)
    
    total_tax = fields.Str(required=False)
    
    processing_method = fields.Str(required=False)
    
    shipping_address = fields.Nested(OrderShippingAddress, required=False)
    
    taxes_included = fields.Boolean(required=False)
    
    financial_status = fields.Str(required=False)
    

