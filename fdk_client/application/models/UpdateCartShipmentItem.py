"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class UpdateCartShipmentItem(BaseSchema):
    # PosCart swagger.json

    
    shipment_type = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    article_uid = fields.Str(required=False)
    

