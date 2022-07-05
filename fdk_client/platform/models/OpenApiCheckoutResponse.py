"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class OpenApiCheckoutResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    order_ref_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    

