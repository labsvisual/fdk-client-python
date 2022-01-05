"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PropBeanConfig import PropBeanConfig


class JsonDocConfig(BaseSchema):
    # Inventory swagger.json

    
    prop_bean_configs = fields.List(fields.Nested(PropBeanConfig, required=False), required=False)
    

