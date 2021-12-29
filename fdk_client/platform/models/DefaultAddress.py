"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




































class DefaultAddress(BaseSchema):
    # Order swagger.json

    
    last_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    province_code = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    id = fields.Int(required=False)
    
    customer_id = fields.Int(required=False)
    
    first_name = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    country_name = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    province = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    zip = fields.Str(required=False)
    

