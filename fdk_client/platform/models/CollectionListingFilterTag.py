"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class CollectionListingFilterTag(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    

