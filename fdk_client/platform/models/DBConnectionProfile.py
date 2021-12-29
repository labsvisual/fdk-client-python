"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class DBConnectionProfile(BaseSchema):
    # Inventory swagger.json

    
    inventory = fields.Str(required=False)
    

