"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






























class BagPrices(BaseSchema):
    # Order swagger.json

    
    cashback = fields.Float(required=False)
    
    refund_credit = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    fynd_credits = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    amount_paid_roundoff = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    refund_amount = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    

