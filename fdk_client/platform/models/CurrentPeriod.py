"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CurrentPeriod(BaseSchema):
    # Billing swagger.json

    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    

