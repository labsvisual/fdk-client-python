"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class PosCartValidator:
    
    class getCart(BaseSchema):
        
        id = fields.Str(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
        
        assign_card_id = fields.Int(required=False)
        
        buy_now = fields.Boolean(required=False)
         
    
    class getCartLastModified(BaseSchema):
        
        id = fields.Str(required=False)
         
    
    class addItems(BaseSchema):
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
        
        buy_now = fields.Boolean(required=False)
         
    
    class updateCart(BaseSchema):
        
        id = fields.Str(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
        
        buy_now = fields.Boolean(required=False)
         
    
    class getItemCount(BaseSchema):
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
         
    
    class getCoupons(BaseSchema):
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
         
    
    class applyCoupon(BaseSchema):
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
        
        p = fields.Boolean(required=False)
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
         
    
    class removeCoupon(BaseSchema):
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
         
    
    class getBulkDiscountOffers(BaseSchema):
        
        item_id = fields.Int(required=False)
        
        article_id = fields.Str(required=False)
        
        uid = fields.Int(required=False)
        
        slug = fields.Str(required=False)
         
    
    class applyRewardPoints(BaseSchema):
        
        id = fields.Str(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
        
        buy_now = fields.Boolean(required=False)
         
    
    class getAddresses(BaseSchema):
        
        cart_id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        mobile_no = fields.Str(required=False)
        
        checkout_mode = fields.Str(required=False)
        
        tags = fields.Str(required=False)
        
        is_default = fields.Boolean(required=False)
         
    
    class addAddress(BaseSchema):
        
        pass 
    
    class getAddressById(BaseSchema):
        
        id = fields.Str(required=False)
        
        cart_id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        mobile_no = fields.Str(required=False)
        
        checkout_mode = fields.Str(required=False)
        
        tags = fields.Str(required=False)
        
        is_default = fields.Boolean(required=False)
         
    
    class updateAddress(BaseSchema):
        
        id = fields.Str(required=False)
         
    
    class removeAddress(BaseSchema):
        
        id = fields.Str(required=False)
         
    
    class selectAddress(BaseSchema):
        
        cart_id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
         
    
    class selectPaymentMode(BaseSchema):
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
         
    
    class validateCouponForPayment(BaseSchema):
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        address_id = fields.Str(required=False)
        
        payment_mode = fields.Str(required=False)
        
        payment_identifier = fields.Str(required=False)
        
        aggregator_name = fields.Str(required=False)
        
        merchant_code = fields.Str(required=False)
         
    
    class getShipments(BaseSchema):
        
        pick_at_store_uid = fields.Int(required=False)
        
        ordering_store_id = fields.Int(required=False)
        
        p = fields.Boolean(required=False)
        
        id = fields.Str(required=False)
        
        address_id = fields.Str(required=False)
        
        area_code = fields.Str(required=False)
        
        order_type = fields.Str(required=False)
         
    
    class updateShipments(BaseSchema):
        
        i = fields.Boolean(required=False)
        
        p = fields.Boolean(required=False)
        
        id = fields.Str(required=False)
        
        address_id = fields.Str(required=False)
        
        order_type = fields.Str(required=False)
         
    
    class checkoutCart(BaseSchema):
        
        id = fields.Str(required=False)
         
    
    class updateCartMeta(BaseSchema):
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
         
    
    class getAvailableDeliveryModes(BaseSchema):
        
        area_code = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getStoreAddressByUid(BaseSchema):
        
        store_uid = fields.Int(required=False)
         
    
    class getCartShareLink(BaseSchema):
        
        pass 
    
    class getCartSharedItems(BaseSchema):
        
        token = fields.Str(required=False)
         
    
    class updateCartWithSharedItems(BaseSchema):
        
        token = fields.Str(required=False)
        
        action = fields.Str(required=False)
         
    