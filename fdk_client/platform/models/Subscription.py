"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SubscriptionCurrentPeriod import SubscriptionCurrentPeriod

from .SubscriptionPauseCollection import SubscriptionPauseCollection

from .SubscriptionTrial import SubscriptionTrial

from .SubscriptionInvoiceSettings import SubscriptionInvoiceSettings













from .Plan import Plan












class Subscription(BaseSchema):
    # Billing swagger.json

    
    current_period = fields.Nested(SubscriptionCurrentPeriod, required=False)
    
    pause_collection = fields.Nested(SubscriptionPauseCollection, required=False)
    
    trial = fields.Nested(SubscriptionTrial, required=False)
    
    invoice_settings = fields.Nested(SubscriptionInvoiceSettings, required=False)
    
    is_active = fields.Boolean(required=False)
    
    cancel_at_period_end = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    subscriber_id = fields.Str(required=False)
    
    plan_id = fields.Str(required=False)
    
    product_suite_id = fields.Str(required=False)
    
    plan_data = fields.Nested(Plan, required=False)
    
    current_status = fields.Str(required=False)
    
    collection_method = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    latest_invoice = fields.Str(required=False)
    

