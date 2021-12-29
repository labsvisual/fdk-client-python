"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema















from .ShipmentTrackResponseBagListItemBreakValues import ShipmentTrackResponseBagListItemBreakValues

from .ShipmentTrackResponseBagListItemStatuses import ShipmentTrackResponseBagListItemStatuses











from .ShipmentTrackResponseBagListItemDpDetails import ShipmentTrackResponseBagListItemDpDetails



from .ShipmentTrackResponseBagListItemsProductImage import ShipmentTrackResponseBagListItemsProductImage
















class ShipmentTrackResponseBagListItem(BaseSchema):
    # Order swagger.json

    
    enable_tracking = fields.Boolean(required=False)
    
    price = fields.Str(required=False)
    
    time_slot = fields.Str(required=False)
    
    product_name = fields.Str(required=False)
    
    can_return = fields.Boolean(required=False)
    
    order_date = fields.Str(required=False)
    
    is_try_at_home = fields.Boolean(required=False)
    
    breakup_values = fields.List(fields.Nested(ShipmentTrackResponseBagListItemBreakValues, required=False), required=False)
    
    statuses = fields.List(fields.Nested(ShipmentTrackResponseBagListItemStatuses, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    bag_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    payment_mode_source = fields.Str(required=False)
    
    dp_details = fields.Nested(ShipmentTrackResponseBagListItemDpDetails, required=False)
    
    product_id = fields.Int(required=False)
    
    product_image = fields.Nested(ShipmentTrackResponseBagListItemsProductImage, required=False)
    
    brand_name = fields.Str(required=False)
    
    price_marked = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    payment_mode = fields.Str(required=False)
    
    fynd_cash_msg = fields.Str(required=False)
    
    delivery_address = fields.Str(required=False)
    

