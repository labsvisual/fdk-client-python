"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ShipmentTrackResponseBagListItemStatusesProgress(BaseSchema):
    # Order swagger.json

    
    title = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    state = fields.Boolean(required=False)
    

