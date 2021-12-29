"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class OptOutInventory(BaseSchema):
    # Configuration swagger.json

    
    store = fields.List(fields.Int(required=False), required=False)
    
    company = fields.List(fields.Int(required=False), required=False)
    

