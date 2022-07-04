"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class SeoDetail(BaseSchema):
    # Catalog swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    

