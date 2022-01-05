"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class ValidateProduct(BaseSchema):
    # Catalog swagger.json

    
    valid = fields.Boolean(required=False)
    

