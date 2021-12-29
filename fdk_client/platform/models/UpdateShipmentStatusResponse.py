"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class UpdateShipmentStatusResponse(BaseSchema):
    # Order swagger.json

    
    shipments = fields.Dict(required=False)
    
    error_shipments = fields.List(fields.Raw(required=False), required=False)
    

