"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class SuccessResponse1(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    

