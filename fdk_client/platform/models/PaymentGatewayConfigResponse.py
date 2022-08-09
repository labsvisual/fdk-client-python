"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class PaymentGatewayConfigResponse(BaseSchema):
    # Payment swagger.json

    
    aggregators = fields.List(fields.Dict(required=False), required=False)
    
    created = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    display_fields = fields.List(fields.Str(required=False), required=False)
    
    excluded_fields = fields.List(fields.Str(required=False), required=False)
    
    success = fields.Boolean(required=False)
    

