"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class EntityChargeRecurring(BaseSchema):
    # Billing swagger.json

    
    interval = fields.Str(required=False)
    

