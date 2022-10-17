"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CartBreakup import CartBreakup



from .SharedCartDetails import SharedCartDetails











from .PaymentSelectionLock import PaymentSelectionLock

from .CartProductInfo import CartProductInfo

from .CartCurrency import CartCurrency





from .ShipmentPromise import ShipmentPromise










class SharedCart(BaseSchema):
    # Cart swagger.json

    
    restrict_checkout = fields.Boolean(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    last_modified = fields.Str(required=False)
    
    shared_cart_details = fields.Nested(SharedCartDetails, required=False)
    
    is_valid = fields.Boolean(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    gstin = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    cart_id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    id = fields.Str(required=False)
    

