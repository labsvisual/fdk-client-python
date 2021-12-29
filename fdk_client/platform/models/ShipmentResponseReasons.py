"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ShipmentResponseReasons(BaseSchema):
    # Order swagger.json

    
    reason_id = fields.Float(required=False)
    
    reason = fields.Str(required=False)
    

