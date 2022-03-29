"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PlatformOrderUserInfo import PlatformOrderUserInfo

from .PlatformDeliveryAddress import PlatformDeliveryAddress

from .Channel import Channel





from .PlatformBreakupValues import PlatformBreakupValues



from .PlatformApplication import PlatformApplication

from .PlatformShipmentDetails import PlatformShipmentDetails





from .ItemsPayments import ItemsPayments




class OrderDetailsItem(BaseSchema):
    # Order swagger.json

    
    user = fields.Nested(PlatformOrderUserInfo, required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    channel = fields.Nested(Channel, required=False)
    
    fyndstore_emp = fields.Dict(required=False)
    
    ordering_store = fields.Dict(required=False)
    
    breakup_values = fields.Nested(PlatformBreakupValues, required=False)
    
    id = fields.Str(required=False)
    
    application = fields.Nested(PlatformApplication, required=False)
    
    shipments = fields.Nested(PlatformShipmentDetails, required=False)
    
    created_at = fields.Str(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    payments = fields.Nested(ItemsPayments, required=False)
    
    payment_methods = fields.Dict(required=False)
    

