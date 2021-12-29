"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class Meta(BaseSchema):
    # Catalog swagger.json

    
    source = fields.Str(required=False)
    

