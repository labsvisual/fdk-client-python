"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute


class PaymentFlow(BaseSchema):
    # Payment swagger.json

    
    rupifi = fields.Nested(AggregatorRoute, required=False)
    
    ccavenue = fields.Nested(AggregatorRoute, required=False)
    
    upi_razorpay = fields.Nested(AggregatorRoute, required=False)
    
    jiopay = fields.Nested(AggregatorRoute, required=False)
    
    epaylater = fields.Nested(AggregatorRoute, required=False)
    
    razorpay = fields.Nested(AggregatorRoute, required=False)
    
    bqr_razorpay = fields.Nested(AggregatorRoute, required=False)
    
    stripe = fields.Nested(AggregatorRoute, required=False)
    
    payubiz = fields.Nested(AggregatorRoute, required=False)
    
    simpl = fields.Nested(AggregatorRoute, required=False)
    
    juspay = fields.Nested(AggregatorRoute, required=False)
    
    mswipe = fields.Nested(AggregatorRoute, required=False)
    
    fynd = fields.Nested(AggregatorRoute, required=False)
    

