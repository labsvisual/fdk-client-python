"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ArticleBrand(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    

