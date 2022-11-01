"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .CartCurrency import CartCurrency

from .CartProductInfo import CartProductInfo

from .CartBreakup import CartBreakup











from .ShipmentPromise import ShipmentPromise



from .PaymentSelectionLock import PaymentSelectionLock


class CartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    gstin = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    buy_now = fields.Boolean(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    

