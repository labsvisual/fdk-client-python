"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Send(BaseSchema):
    # Inventory swagger.json

    
    raw = fields.Boolean(required=False)
    
    processed = fields.Boolean(required=False)
    

