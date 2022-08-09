"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class OrderQuantity(BaseSchema):
    # Catalog swagger.json

    
    maximum = fields.Int(required=False)
    
    minimum = fields.Int(required=False)
    
    is_set = fields.Boolean(required=False)
    

