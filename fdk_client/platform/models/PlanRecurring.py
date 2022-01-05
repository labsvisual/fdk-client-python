"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PlanRecurring(BaseSchema):
    # Billing swagger.json

    
    interval = fields.Str(required=False)
    
    interval_count = fields.Float(required=False)
    

