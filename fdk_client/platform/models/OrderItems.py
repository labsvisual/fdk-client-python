"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PlatformOrderUserInfo import PlatformOrderUserInfo

from .PlatformDeliveryAddress import PlatformDeliveryAddress

from .Channel import Channel



from .PlatformApplication import PlatformApplication

from .PlatformShipment import PlatformShipment






class OrderItems(BaseSchema):
    # Order swagger.json

    
    user = fields.Nested(PlatformOrderUserInfo, required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    channel = fields.Nested(Channel, required=False)
    
    id = fields.Str(required=False)
    
    application = fields.Nested(PlatformApplication, required=False)
    
    shipments = fields.Nested(PlatformShipment, required=False)
    
    created_at = fields.Str(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    

