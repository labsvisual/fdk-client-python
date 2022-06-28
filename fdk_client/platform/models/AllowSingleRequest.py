"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class AllowSingleRequest(BaseSchema):
    # Catalog swagger.json

    
    allow_single = fields.Boolean(required=False)
    

