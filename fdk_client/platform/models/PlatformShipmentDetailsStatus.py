"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




















class PlatformShipmentDetailsStatus(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    bag_list = fields.List(fields.Int(required=False), required=False)
    
    created_at = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    progress = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    current_shipment_status = fields.Str(required=False)
    
    color_code = fields.Str(required=False)
    

