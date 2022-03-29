"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PlatformShipmentDetailsStatus import PlatformShipmentDetailsStatus

from .BagsDetails import BagsDetails

from .ShipmentPrices import ShipmentPrices

from .ShipmentBreakupValues import ShipmentBreakupValues



from .DpDetails import DpDetails



from .ShipmentInvoice import ShipmentInvoice

from .PlatformFulfillingStore import PlatformFulfillingStore

from .Payments import Payments

from .ShipmentGst import ShipmentGst

from .Company import Company

from .PlatformShipmentDetailsBrand import PlatformShipmentDetailsBrand











from .Promise import Promise

from .ShipmentTrackingDetails import ShipmentTrackingDetails























from .ShipmentDates import ShipmentDates


class PlatformShipmentDetails(BaseSchema):
    # Order swagger.json

    
    status = fields.Nested(PlatformShipmentDetailsStatus, required=False)
    
    bags = fields.Nested(BagsDetails, required=False)
    
    prices = fields.Nested(ShipmentPrices, required=False)
    
    breakup_values = fields.Nested(ShipmentBreakupValues, required=False)
    
    id = fields.Str(required=False)
    
    dp_details = fields.Nested(DpDetails, required=False)
    
    payment_methods = fields.Dict(required=False)
    
    invoice = fields.Nested(ShipmentInvoice, required=False)
    
    fulfilling_store = fields.Nested(PlatformFulfillingStore, required=False)
    
    payments = fields.Nested(Payments, required=False)
    
    gst = fields.Nested(ShipmentGst, required=False)
    
    company = fields.Nested(Company, required=False)
    
    brand = fields.Nested(PlatformShipmentDetailsBrand, required=False)
    
    coupon = fields.Dict(required=False)
    
    order_source = fields.Str(required=False)
    
    is_not_fynd_source = fields.Boolean(required=False)
    
    can_break = fields.Dict(required=False)
    
    comment = fields.Str(required=False)
    
    promise = fields.Nested(Promise, required=False)
    
    tracking_details = fields.Nested(ShipmentTrackingDetails, required=False)
    
    is_fynd_coupon = fields.Boolean(required=False)
    
    order_type = fields.Str(required=False)
    
    total_shipment_bags = fields.Int(required=False)
    
    pod = fields.Dict(required=False)
    
    lock_status = fields.Boolean(required=False)
    
    priority = fields.Float(required=False)
    
    priority_text = fields.Str(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    credit_note_id = fields.Str(required=False)
    
    auto_trigger_dp_assignment = fields.Boolean(required=False)
    
    packaging_type = fields.Str(required=False)
    
    dates = fields.Nested(ShipmentDates, required=False)
    

