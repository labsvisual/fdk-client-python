"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PlatformShipmentStatus import PlatformShipmentStatus

from .Bags import Bags

from .ShipmentPrices import ShipmentPrices



from .ShipmentGst import ShipmentGst












class PlatformShipment(BaseSchema):
    # Order swagger.json

    
    status = fields.Nested(PlatformShipmentStatus, required=False)
    
    bags = fields.Nested(Bags, required=False)
    
    prices = fields.Nested(ShipmentPrices, required=False)
    
    id = fields.Str(required=False)
    
    gst = fields.Nested(ShipmentGst, required=False)
    
    priority = fields.Float(required=False)
    
    priority_text = fields.Str(required=False)
    
    lock_status = fields.Boolean(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    total_shipment_bags = fields.Int(required=False)
    

