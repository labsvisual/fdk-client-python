"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class CatalogMasterConfig(BaseSchema):
    # Inventory swagger.json

    
    source_slug = fields.Str(required=False)
    

