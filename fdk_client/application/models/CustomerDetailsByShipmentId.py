"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class CustomerDetailsByShipmentId(BaseSchema):
    # Order swagger.json

    
    order_id = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    country = fields.Str(required=False)
    

