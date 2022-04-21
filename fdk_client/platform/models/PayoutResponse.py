"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class PayoutResponse(BaseSchema):
    # Payment swagger.json

    
    unique_transfer_no = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    transfer_type = fields.Str(required=False)
    
    payouts = fields.Dict(required=False)
    
    created = fields.Boolean(required=False)
    
    users = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    bank_details = fields.Dict(required=False)
    
    aggregator = fields.Str(required=False)
    
    payment_status = fields.Str(required=False)
    

