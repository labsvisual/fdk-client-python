"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class BagCurrStatus(BaseSchema):
    # Order swagger.json

    
    enable_tracking = fields.Boolean(required=False)
    
    is_customer_return_allowed = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_returnable = fields.Boolean(required=False)
    
    can_be_cancelled = fields.Boolean(required=False)
    

