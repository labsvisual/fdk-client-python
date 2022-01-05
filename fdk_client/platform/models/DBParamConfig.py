"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class DBParamConfig(BaseSchema):
    # Inventory swagger.json

    
    params = fields.Dict(required=False)
    

