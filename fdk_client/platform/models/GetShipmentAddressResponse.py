"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .DataShipmentAddress import DataShipmentAddress




class GetShipmentAddressResponse(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Nested(DataShipmentAddress, required=False)
    
    success = fields.Boolean(required=False)
    

