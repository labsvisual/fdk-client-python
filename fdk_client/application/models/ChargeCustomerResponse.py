"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class ChargeCustomerResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    delivery_address_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    

