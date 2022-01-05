"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .StageItem import StageItem


class OrderLanesCount(BaseSchema):
    # Order swagger.json

    
    stages = fields.List(fields.Nested(StageItem, required=False), required=False)
    

