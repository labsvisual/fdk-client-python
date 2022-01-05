"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class ShipmentDates(BaseSchema):
    # Order swagger.json

    
    due_date = fields.Str(required=False)
    

