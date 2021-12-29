"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PlanRecurring import PlanRecurring






































class Plan(BaseSchema):
    # Billing swagger.json

    
    recurring = fields.Nested(PlanRecurring, required=False)
    
    is_trial_plan = fields.Boolean(required=False)
    
    plan_group = fields.Str(required=False)
    
    tag_lines = fields.List(fields.Str(required=False), required=False)
    
    currency = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    trial_period = fields.Float(required=False)
    
    addons = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    product_suite_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    

