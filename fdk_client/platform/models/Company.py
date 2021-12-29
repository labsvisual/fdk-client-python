"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
































class Company(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    company_type = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    company_name = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    pan_no = fields.Str(required=False)
    
    return_allowed = fields.Boolean(required=False)
    
    meta = fields.Str(required=False)
    
    exchange_allowed = fields.Boolean(required=False)
    
    agreement_start_date = fields.Str(required=False)
    
    exchange_within_days = fields.Int(required=False)
    
    payment_procesing_charge = fields.Int(required=False)
    
    fynd_a_fit_available = fields.Boolean(required=False)
    
    modified_on = fields.Str(required=False)
    
    return_within_days = fields.Int(required=False)
    

