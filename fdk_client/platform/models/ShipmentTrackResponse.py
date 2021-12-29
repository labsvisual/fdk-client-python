"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ShipmentTrackResponseBagListItem import ShipmentTrackResponseBagListItem






class ShipmentTrackResponse(BaseSchema):
    # Order swagger.json

    
    bag_list = fields.List(fields.Nested(ShipmentTrackResponseBagListItem, required=False), required=False)
    
    message = fields.Str(required=False)
    
    order_value = fields.Int(required=False)
    

