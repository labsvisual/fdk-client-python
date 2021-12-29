"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .FailOrder import FailOrder


class FailedOrders(BaseSchema):
    # Order swagger.json

    
    orders = fields.Nested(FailOrder, required=False)
    

