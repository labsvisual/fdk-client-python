"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class OrderQuantity(BaseSchema):
    # Catalog swagger.json

    
    is_set = fields.Boolean(required=False)
    
    minimum = fields.Int(required=False)
    
    maximum = fields.Int(required=False)
    

