"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









































from .DefaultAddress import DefaultAddress


class Customer(BaseSchema):
    # Order swagger.json

    
    created_at = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    last_name = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    last_order_id = fields.Int(required=False)
    
    note = fields.Str(required=False)
    
    verified_email = fields.Boolean(required=False)
    
    phone = fields.Str(required=False)
    
    accepts_marketing = fields.Boolean(required=False)
    
    first_name = fields.Str(required=False)
    
    tags = fields.Str(required=False)
    
    last_order_name = fields.Str(required=False)
    
    orders_count = fields.Int(required=False)
    
    total_spent = fields.Str(required=False)
    
    tax_exempt = fields.Boolean(required=False)
    
    currency = fields.Str(required=False)
    
    accepts_marketing_updated_at = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    admin_graphql_api_id = fields.Str(required=False)
    
    default_address = fields.Nested(DefaultAddress, required=False)
    

