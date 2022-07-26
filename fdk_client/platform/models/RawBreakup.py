"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


























class RawBreakup(BaseSchema):
    # Cart swagger.json

    
    you_saved = fields.Float(required=False)
    
    gst_charges = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    mrp_total = fields.Float(required=False)
    
    coupon = fields.Float(required=False)
    
    subtotal = fields.Float(required=False)
    
    fynd_cash = fields.Float(required=False)
    
    cod_charge = fields.Float(required=False)
    
    total = fields.Float(required=False)
    
    convenience_fee = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    vog = fields.Float(required=False)
    

