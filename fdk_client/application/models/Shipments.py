"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .BreakupValues import BreakupValues









from .TrackingDetails import TrackingDetails







from .Prices import Prices







from .DeliveryAddress import DeliveryAddress

from .Invoice import Invoice





from .Promise import Promise

from .FulfillingStore import FulfillingStore

from .Bags import Bags



from .ShipmentPayment import ShipmentPayment



from .ShipmentStatus import ShipmentStatus

from .ShipmentUserInfo import ShipmentUserInfo



from .ShipmentTotalDetails import ShipmentTotalDetails


class Shipments(BaseSchema):
    # Order swagger.json

    
    order_id = fields.Str(required=False)
    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    
    track_url = fields.Str(required=False)
    
    traking_no = fields.Str(required=False)
    
    awb_no = fields.Str(required=False)
    
    dp_name = fields.Str(required=False)
    
    tracking_details = fields.List(fields.Nested(TrackingDetails, required=False), required=False)
    
    beneficiary_details = fields.Boolean(required=False)
    
    can_return = fields.Boolean(required=False)
    
    can_break = fields.Dict(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    need_help_url = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    total_bags = fields.Int(required=False)
    
    delivery_address = fields.Nested(DeliveryAddress, required=False)
    
    invoice = fields.Nested(Invoice, required=False)
    
    comment = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    promise = fields.Nested(Promise, required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    bags = fields.List(fields.Nested(Bags, required=False), required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    payment = fields.Nested(ShipmentPayment, required=False)
    
    shipment_created_at = fields.Str(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    user_info = fields.Nested(ShipmentUserInfo, required=False)
    
    size_info = fields.Dict(required=False)
    
    total_details = fields.Nested(ShipmentTotalDetails, required=False)
    

