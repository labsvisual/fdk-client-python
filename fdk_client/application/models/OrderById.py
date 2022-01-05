"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderSchema import OrderSchema


class OrderById(BaseSchema):
    # Order swagger.json

    
    order = fields.Nested(OrderSchema, required=False)
    

