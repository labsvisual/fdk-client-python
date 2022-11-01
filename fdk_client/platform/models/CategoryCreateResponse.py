"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CategoryCreateResponse(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    message = fields.Str(required=False)
    

