"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Items import Items

from .Page import Page


class BulkAssetResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(Items, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

