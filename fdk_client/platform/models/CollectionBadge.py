"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CollectionBadge(BaseSchema):
    # Catalog swagger.json

    
    text = fields.Str(required=False)
    
    color = fields.Str(required=False)
    

