"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class PaymentStatusUpdateResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    retry = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    redirect_url = fields.Str(required=False)
    

