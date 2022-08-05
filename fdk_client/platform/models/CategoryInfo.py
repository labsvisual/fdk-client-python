"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CategoryInfo(BaseSchema):
    # Cart swagger.json

    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    

