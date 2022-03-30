"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class PaymentStatusUpdateResponse(BaseSchema):
    # Payment swagger.json

    
    retry = fields.Boolean(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    

