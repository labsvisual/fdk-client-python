"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema















from .ReceivedAt import ReceivedAt


class AbandonCartsDetail(BaseSchema):
    # Analytics swagger.json

    
    properties_cart_id = fields.Str(required=False)
    
    context_traits_first_name = fields.Str(required=False)
    
    context_traits_last_name = fields.Str(required=False)
    
    context_traits_phone_number = fields.Str(required=False)
    
    context_traits_email = fields.Str(required=False)
    
    context_app_application_id = fields.Str(required=False)
    
    properties_breakup_values_raw_total = fields.Str(required=False)
    
    received_at = fields.Nested(ReceivedAt, required=False)
    

