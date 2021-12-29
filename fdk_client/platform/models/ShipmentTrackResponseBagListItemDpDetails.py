"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ShipmentTrackResponseBagListItemDpDetails(BaseSchema):
    # Order swagger.json

    
    tracking_no = fields.Str(required=False)
    
    courier = fields.Str(required=False)
    

