"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class SubscriptionConfigResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    config = fields.Dict(required=False)
    
    aggregator = fields.Str(required=False)
    

