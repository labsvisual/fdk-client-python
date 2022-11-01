"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class CartMetaRequest(BaseSchema):
    # Cart swagger.json

    
    pick_up_customer_details = fields.Dict(required=False)
    
    gstin = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    

