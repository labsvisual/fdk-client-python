"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Charges import Charges


class DeliveryCharges(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    
    charges = fields.Nested(Charges, required=False)
    

