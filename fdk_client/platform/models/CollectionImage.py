"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CollectionImage(BaseSchema):
    # Catalog swagger.json

    
    url = fields.Str(required=False)
    
    aspect_ratio = fields.Str(required=False)
    

